# Exercise 18:Volume of a Cylinder

# The volume of a cylinder can be computed by multiplying the area of its circular
# base by its height. Write a program that reads the radius of the cylinder, along with
# its height, from the user and computes its volume. Display the result rounded to one
# decimal place.

# Solution:

import math

while True:
    try:
        # take input from user
        radius = float(
            input("\nEnter the radius of the cylinder (cm or m) : "))

        unit = input("\nEnter the unit used (cm or m): ").lower()
        if unit not in ['cm', 'm']:
            print("Please, enter 'cm' or 'm' as your unit")
            continue

        height = float(
            input(f"\nEnter the height of the cylinder in {unit}: "))

        if radius <= 0 or height <= 0:
            print("Radius and height must be positive values.")
            continue

        # calculate the volume
        volume = math.pi * (radius ** 2) * height

        # print the result
        unit_cubed = f"{unit}\u00b3"
        print(f"\nThe volume of the cylinder is {volume:.1f} {unit_cubed}")

        while True:
            calculate_again = input(
                """\nWould you like to make another calculation? : 
                        \nEnter \n\nY for YES \n\nN for NO: """).upper()
            if calculate_again in ['Y', 'YES', 'N', 'NO']:
                break
            print("Invalid input! Please enter Y or N.")

        if calculate_again in ['N', 'NO']:
            print("\nThank you for using the calculator!")
            break

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
