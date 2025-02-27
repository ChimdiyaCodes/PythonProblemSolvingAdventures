# Exercise 37: Name that Shape

# Write a program that determines the name of a shape from its number of sides. Read
# the number of sides from the user and then report the appropriate name as part of
# a meaningful message. Your program should support shapes with anywhere from 3
# up to (and including) 10 sides. If a number of sides outside of this range is entered
# then your program should display an appropriate error message.

# solution:

while True:
    try:
        # Prompt the user to enter the number of sides
        num_sides = int(input("\nEnter the number of sides (3-10): "))

        # Determine the shape based on the number of sides
        if num_sides == 3:
            shape = "Triangle"
        elif num_sides == 4:
            shape = "Quadrilateral"
        elif num_sides == 5:
            shape = "Pentagon"
        elif num_sides == 6:
            shape = "Hexagon"
        elif num_sides == 7:
            shape = "Heptagon"
        elif num_sides == 8:
            shape = "Octagon"
        elif num_sides == 9:
            shape = "Nonagon"
        elif num_sides == 10:
            shape = "Decagon"
        else:
            # Handle invalid input
            print("Error: The number of sides must be between 3 and 10 (inclusive).")
            continue

        # Display the result
        print(f"\nA shape with {num_sides} sides is a {shape}.")
        break

    except ValueError:
        print("Invalid input! Please enter a numeric value.")
