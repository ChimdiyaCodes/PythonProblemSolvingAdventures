# Exercise 101: Reduce a Fraction to Lowest Terms

# Write a function that takes two positive integers that represent the numerator and
# denominator of a fraction as its only two parameters. The body of the function
# should reduce the fraction to lowest terms and then return both the numerator and
# denominator of the reduced fraction as its result. For example, if the parameters
# passed to the function are 6 and 63 then the function should return 2 and 21. Include
# a main program that allows the user to enter a numerator and denominator. Then
# your program should display the reduced fraction.

# solution

import math


def reduce_fraction(numerator, denominator):
    # Reduce a fraction to its lowest terms.
    gcd = math.gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd


def get_positive_integer(prompt):
    # Prompt user for a positive integer with validation.
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    print("\n---This Program Reduces a Fraction to it's Lowest Terms---")

    # Get validated inputs
    numerator = get_positive_integer(
        "\nEnter the numerator (positive integer): ")

    while True:
        denominator = get_positive_integer(
            "\nEnter the denominator (positive integer and not zero): ")
        if denominator == 0:
            print("Denominator cannot be zero. Please enter a valid denominator.")
        else:
            break

    # Reduce the fraction
    reduced_numerator, reduced_denominator = reduce_fraction(
        numerator, denominator)

    # Display the result
    print(f"\nReduced fraction: {reduced_numerator}/{reduced_denominator}")


if __name__ == "__main__":
    main()
