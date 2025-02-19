# Exercise 21: Area of a Triangle

# The area of a triangle can be computed using the following formula, where b is the
# length of the base of the triangle, and h is its height:
# area = b × h / 2
# Write a program that allows the user to enter values for b and h. The program
# should then compute and display the area of a triangle with base length b and height h.

# Solution:

while True:
    try:
        # Take input for base
        base = float(input("\nEnter the base of the triangle (cm or m): "))
        if base <= 0:
            print("Base must be a positive value.")
            continue

        # Take input for unit
        unit = input("\nEnter the unit used (cm or m): ").lower()
        if unit not in ['cm', 'm']:
            print("Please, enter 'cm' or 'm' as your unit.")
            continue

        # Take input for height
        height = float(
            input(f"\nEnter the height of the triangle in {unit}: "))
        if height <= 0:
            print("Height must be a positive value.")
            continue

        # Calculate the area
        area = base * height / 2

        # Display the result
        print(f"\nThe area of the triangle is {area:.2f} {unit}\u00B2")
        break

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
