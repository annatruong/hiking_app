from calculation import get_rating, get_average_gradient_percentage, get_average_climb
from inputs import get_ascent, get_distance

# Prints results to screen
def show_results(distance, ascent, average_gradient, average_climb, rating):
    print("\n================ HIKE EVALUATION ================\n")
    print(f"Distance: {distance} km")
    print(f"Ascent: {ascent} m")
    print(f"Average gradient: {average_gradient}%")
    print(f"Average climb: {average_climb} m/km")
    print(f"Difficulty: {rating}")
    print("\n=================================================\n")

# Asks user if they want to run the application again
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

    while True:
        # Get ascent and distance from user
        ascent = get_ascent()
        distance = get_distance()

        # Calculate average gradient and average climb
        average_gradient = get_average_gradient_percentage(ascent, distance)
        average_climb = get_average_climb(ascent, distance)
        rating = get_rating(average_climb)

        # Display results
        show_results(distance, ascent, average_gradient, average_climb, rating)

        # Check if user wants to continue
        if not run_again():
            break
        

main()
