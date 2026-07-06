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

def show_results(distance, ascent, average_gradient, average_climb, rating):
    print("\n================ HIKE EVALUATION ================\n")
    print(f"Distance: {distance} km")
    print(f"Ascent: {ascent} m")
    print(f"Average gradient: {average_gradient}%")
    print(f"Average climb: {average_climb} m/km")
    print(f"Difficulty: {rating}")
    print("\n=================================================\n")

def run_again():
    while True:
        resume = input("Do you want to calculate another hike? (y/n): ").lower()
        print()
        if resume == "n":
            return False
        elif resume == "y":
            return True
        else:
            print("Incorrect value. Please enter 'y' if you wish to continue or 'n' if you would like to quit.\n")

def main():

    print(r"""
       /\    /\    /\    /\    /\    /\   
      /  \  /  \  /  \  /  \  /  \  /  \  
     /____\/____\/____\/____\/____\/____\  

              🥾 HIKING APP 🥾
     Gradient • Climb • Difficulty Rating
        How steep is your adventure?
    """)

    run = True
    while run:
        # Get ascent and distance from user
        ascent = int(input("Enter the total ascent(m): "))
        distance = float(input("Enter the total distance(km): "))

        # Calculate average gradient and average climb
        average_gradient = get_average_gradient_percentage(ascent, distance)
        average_climb = get_average_climb(ascent, distance)
        rating = get_rating(average_climb)

        # Display results
        show_results(distance, ascent, average_gradient, average_climb, rating)

        # Check if user wants to continue
        run = run_again()
        

main()
