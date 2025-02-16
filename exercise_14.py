# Exercise 14: Height Units

# Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
# the user, followed by a number of inches. Once these values are read, your program
# should compute and display the equivalent number of centimeters.
# Hint: One foot is 12 inches. One inch is 2.54 centimeters.

# Solution:

while True:
    try:

        # take input from the user

        print("\nYou will be asked to enter your height below. Enter only the feet first. You will also get a chance to enter the remaining inches afterwards.")

        height_in_feet = int(input("\nEnter your height in feet only: "))

        height_in_inches = int(
            input("\nNow, enter the remaining height in inches: "))

        # convert the feet to inches

        feet_to_inches = height_in_feet * 12

        # add the additional inches

        total_inches = feet_to_inches + height_in_inches

        # convert inches to cm

        height_in_cm = total_inches * 2.54

        # display result

        print(f"\nYour total height in centimetres is {height_in_cm}cm")
        break

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
