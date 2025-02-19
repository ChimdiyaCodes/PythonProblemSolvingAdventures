# Exercise 22: Area of a Triangle (Again)

# In the previous exercise you created a program that computed the area of a triangle
# when the length of its base and its height were known. It is also possible to compute
# the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
# be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
# can be calculated using the following formula:
# area =  √ s × (s − s1) × (s − s2) × (s − s3)
# Develop a program that reads the lengths of the sides of a triangle from the user and
# displays its area.

# Solution:

import math

while True:
    try:
        # Take input for unit
        unit = input("\nEnter the unit used (cm or m): ").lower()

        # validate unit
        if unit not in ['cm', 'm']:
            print("Invalid unit. Please enter either 'cm' or 'm'.")
            continue

        # Input side lengths
        s1 = float(input(f"\nEnter the length of side 1 in {unit}: "))
        s2 = float(input(f"\nEnter the length of side 2 in {unit}: "))
        s3 = float(input(f"\nEnter the length of side 3 in {unit}: "))

        # Check the triangle inequality theorem (this will catch negative values too)
        if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:

            # compute the semi-perimeter
            s = (s1 + s2 + s3) / 2

            # compute the area
            area = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))

            # display results
            print(f"\nTriangle Details:")
            print(f"Sides: {s1:.2f}, {s2:.2f}, {s3:.2f} {unit}")
            print(f"The Area of the triangle: {area:.2f} {unit}²")
            break
        else:
            print("\nThese sides cannot form a valid triangle.")
            print("The sum of any two sides must be greater than the third side.")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")
