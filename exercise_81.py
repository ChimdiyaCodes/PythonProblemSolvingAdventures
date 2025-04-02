# Exercise 81: Compute the Hypotenuse

# Write a function that takes the lengths of the two shorter sides of a right triangle as
# its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
# theorem, as the function’s result. Include a main program that reads the lengths of
# the shorter sides of a right triangle from the user, uses your function to compute the
# length of the hypotenuse, and displays the result.

# solution:

import math


def calculate_hypotenuse(a, b):
    """
    Calculate the hypotenuse of a right triangle using the Pythagorean theorem.

    Parameters:
    a (float): Length of the first side
    b (float): Length of the second side

    Returns:
    float: Length of the hypotenuse
    """
    return math.sqrt(a**2 + b**2)


def get_positive_number(prompt):
    """
    Continuously prompt the user until a valid positive number is entered.

    Parameters:
    prompt (str): The message to display to the user

    Returns:
    float: The valid positive number entered by the user
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("Right Triangle Hypotenuse Calculator")
    print("------------------------------------")

    # Get valid input for both sides
    side1 = get_positive_number("\nEnter the length of the first side: ")
    side2 = get_positive_number("Enter the length of the second side: ")

    # Calculate the hypotenuse
    hypotenuse = calculate_hypotenuse(side1, side2)

    # Display the result
    print(
        f"\nThe hypotenuse of a right triangle with sides {side1} and {side2} is: {hypotenuse:.2f}")


if __name__ == "__main__":
    main()
