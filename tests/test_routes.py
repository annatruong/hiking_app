def test_homepage_loads(client):
    response = client.get("/")
    html = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Hike Calculator" in html
    assert "<form" in html
    assert "Distance" in html
    assert "Ascent" in html

def test_results_redirects(client):
    response = client.post(
        "/",
        data={
            "ascent": 350,
            "distance": 18,
            "submit": "Calculate"
        }
    )

    assert response.status_code == 302

def test_results_shows(client):
    response = client.post(
        "/",
        data={
            "ascent": 350,
            "distance": 18,
            "submit": "Calculate"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Easy" in response.data


# The browser displays native validation messages,
# but these are not part of the Flask response.
# Therefore, test that invalid submissions do not produce results.

def test_ascent_validation(client):
    response = client.post(
        "/",
        data={
            "ascent": -1,
            "distance": 18,
            "submit": "Calculate"
        },
        follow_redirects=True
    )
    assert b"Average gradient" not in response.data

def test_distance_validation(client):
    response = client.post(
        "/",
        data={
            "ascent": 400,
            "distance": 0,
            "submit": "Calculate"
        },
        follow_redirects=True
    )
    assert b"Average gradient" not in response.data