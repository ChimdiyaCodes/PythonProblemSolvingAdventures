# Exercise 16: Area and Volume

# Write a program that begins by reading a radius, r, from the user. The program will
# continue by computing and displaying the area of a circle with radius r and the
# volume of a sphere with radius r. Use the pi constant in the math module in your
# calculations.
# Hint: The area of a circle is computed using the formula area = πr 2. The
# volume of a sphere is computed using the formula volume = 4
# 3πr 3.

# solution:

while True:
    try:
        import math

        # Take user input for radius
        r = float(input("\nEnter the radius: "))

        # Compute the area of the circle
        area = math.pi * r**2

        # Compute the volume of the sphere
        volume = (4/3) * math.pi * r**3

        # Display the results
        print(f"The area of the circle is: {area:.2f}")
        print(f"The volume of the sphere is: {volume:.2f}")

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
