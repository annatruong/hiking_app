# Get ascent from user
def get_ascent():
    while True:
        try:
            ascent = int(input("Enter the total ascent(m): "))
            if ascent < 0:
                raise ValueError()
        except ValueError:
            print("Incorrect value. Ascent must be a positive number.")
        else:
            return ascent

# Get distance from user
def get_distance():
    while True:
        try:
            distance = float(input("Enter the total distance(km): "))
            if distance <= 0:
                raise ValueError()
        except ValueError:
            print("Incorrect value. Distance must be a postive number greater than 0.")
        else:
            return distance