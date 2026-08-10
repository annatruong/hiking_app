from calculation import convert_km_to_m, get_average_gradient_percentage, get_average_climb, get_rating

def test_convert_km_m():
    assert convert_km_to_m(20) == 20000
    assert convert_km_to_m(1) == 1000
    assert convert_km_to_m(0) == 0

def test_get_average_gradient_percentage():
    assert get_average_gradient_percentage(350, 18) == 1.9
    assert get_average_gradient_percentage(600, 10) == 6.0
    assert get_average_gradient_percentage(0, 25) == 0.0


def test_get_average_climb():
    assert get_average_climb(350, 18) == 19
    assert get_average_climb(600, 10) == 60
    assert get_average_climb(0, 25) == 0

def test_get_rating():
    assert get_rating(19) == "🟢 Easy"
    assert get_rating(35) == "🟡 Moderate"
    assert get_rating(55) == "🟠 Challenging"
    assert get_rating(75) == "🔴 Hard"
    assert get_rating(100) == "⚫️ Very Hard"