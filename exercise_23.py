# Exercise 23: Area of a Regular Polygon

# A polygon is regular if its sides are all the same length and the angles between all of
# the adjacent sides are equal. The area of a regular polygon can be computed using
# the following formula, where s is the length of a side and n is the number of sides:

# area = n × s² /4 × tan (π/n)
# Write a program that reads s and n from the user and then displays the area of a
# regular polygon constructed from these values.

# Solution:

import math

while True:
    try:
        # take input from the user

        number_of_sides = int(
            input("\nEnter the number of sides the polygon has: "))

        # validate number of sides
        if number_of_sides < 3:
            print("That's an invalid polygon! A valid poygon has 3 or more sides")
            continue

        side_length = float(
            input("\nEnter the length of each side of the polygon in cm or m: "))

        # validate side length
        if side_length <= 0:
            print("The length of the sides must be a positive value.")
            continue

        # Take input for unit
        unit = input("\nEnter the unit used in the length(cm or m): ").lower()

        # validate unit
        if unit not in ['cm', 'm']:
            print("Invalid unit. Please enter either 'cm' or 'm'.")
            continue

        # compute the area

        area = (number_of_sides * side_length**2) / \
            (4 * math.tan(math.pi / number_of_sides))

        # display results
        print(f"""
        
        \nDetails of the polygon:
Number of sides: {number_of_sides}
Length of each side: {side_length}{unit}
        \nThe area of the polygon: {area:.2f}{unit}²
            
    """)
        break

    except ValueError:
        print("Invalid input. Please enter numeric values only.")
