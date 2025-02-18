# Exercise 19: Free Fall

# Create a program that determines how quickly an object is traveling when it hits the
# ground. The user will enter the height from which the object is dropped in meters (m).
# Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
# due to gravity is 9.8 m/s2.

# Solution:

from math import sqrt

while True:
    try:

        # constants

        initial_velocity = 0
        acceleration = 9.8

        # take user input

        height = float(
            input("\nEnter the height from which the object is dropped (in metres) : "))

        # validate input

        if height < 0:
            print("Height cannot be negative. Please enter a positive value.")
            continue

        # calculate final velocity

        final_velocity = sqrt(initial_velocity**2 + 2 * acceleration * height)

        # display the result

        print(
            f"\nThe final velocity of the object when it hits the ground is {final_velocity:.2f} m/s.")
        break

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
