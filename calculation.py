# Converts kilometres to metres
def convert_km_to_m(kilometres):
    return kilometres * 1000
# Calculates the average gradient using ascent and distance. Returns value in 1 decimal place
def get_average_gradient_percentage(ascent, distance):
    return round((ascent / convert_km_to_m(distance)) * 100, 1)

# Calculates ascent per kilometre
def get_average_climb(ascent, distance):
    return round(ascent / distance)

# Get rating base of average climb (m/km)
def get_rating(m_per_km):
    if m_per_km < 20:
        return "🟢 Easy"
    elif 20 <= m_per_km < 40:
        return "🟡 Moderate"
    elif 40 <= m_per_km < 60:
        return "🟠 Challenging"
    elif 60 <= m_per_km < 80:
        return "🔴 Hard"
    else:
        return "⚫️ Very Hard"

# Calculate average gradient, average climb and rating
def get_hike_estimation(ascent, distance):
    average_gradient = get_average_gradient_percentage(ascent, distance)
    average_climb = get_average_climb(ascent, distance)
    rating = get_rating(average_climb)
    return {"average_gradient": average_gradient, "average_climb": average_climb, "rating": rating}