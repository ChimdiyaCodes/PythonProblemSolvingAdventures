# Exercise 12: Distance Between Two Points on Earth

# The surface of the Earth is curved, and the distance between degrees of longitude
# varies with latitude. As a result, finding the distance between two points on the surface
# of the Earth is more complicated than simply using the Pythagorean theorem.
# Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
# surface. The distance between these points, following the surface of the Earth, in
# kilometers is:
# distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
# The value 6371.01 in the previous equation wasn’t selected at random. It is
# the average radius of the Earth in kilometers.
# Create a program that allows the user to enter the latitude and longitude of two
# points on the Earth in degrees. Your program should display the distance between
# the points, following the surface of the earth, in kilometers.

# Hint: Python’s trigonometric functions operate in radians. As a result, you will
# need to convert the user’s input from degrees to radians before computing the
# distance with the formula discussed previously. The math module contains a
# function named radians which converts from degrees to radians.

import math


def calculate_distance():
    while True:
        try:
            # Get the latitude and longitude of the first point
            t1_degree = float(
                input("\nEnter the latitude of the first point (in degrees): "))
            g1_degree = float(
                input("\nEnter the longitude of the first point (in degrees): "))

            # Validate latitude and longitude of the first point
            if not (-90 <= t1_degree <= 90):
                print("Error: Latitude must be between -90 and 90 degrees.")
                continue
            if not (-180 <= g1_degree <= 180):
                print("Error: Longitude must be between -180 and 180 degrees.")
                continue

            # Get the latitude and longitude of the second point
            t2_degree = float(
                input("\nEnter the latitude of the second point (in degrees): "))
            g2_degree = float(
                input("\nEnter the longitude of the second point (in degrees): "))

            # Validate latitude and longitude of the second point
            if not (-90 <= t2_degree <= 90):
                print("Error: Latitude must be between -90 and 90 degrees.")
                continue
            if not (-180 <= g2_degree <= 180):
                print("Error: Longitude must be between -180 and 180 degrees.")
                continue

            # Convert degrees to radians
            t1 = math.radians(t1_degree)
            g1 = math.radians(g1_degree)
            t2 = math.radians(t2_degree)
            g2 = math.radians(g2_degree)

            # Calculate the distance using the formula
            distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) +
                                           math.cos(t1) * math.cos(t2) *
                                           math.cos(g1 - g2))

            # Display the result
            print(
                f"\nThe distance between the points is {distance:.2f} kilometers.")

            # Ask if the user wants to calculate again
            while True:
                calculate_again = input(
                    """\nWould you like to make another calculation? : 
                    \nEnter \n\nY for YES \n\nN for NO: """)
                if calculate_again.upper() in ['Y', 'YES']:
                    break  # Break the inner loop to do another calculation
                elif calculate_again.upper() in ['N', 'NO']:
                    print("\nThank you for using the calculator!")
                    return  # Exit the function (and program)
                else:
                    print("\nInvalid input! Please enter Y for yes or N for no.")
                    continue  # Keep asking for valid input

        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# Run the program
calculate_distance()
