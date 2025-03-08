# Exercise 50: Roots of a Quadratic Function

# A univariate quadratic function has the form f (x) = ax2 + bx + c, where a, b and
# c are constants, and a is non-zero. The roots of a quadratic function can be found
# by finding the values of x that satisfy the quadratic equation ax2 + bx + c = 0. A
# quadratic function may have 0, 1 or 2 real roots. These roots can be computed using
# the quadratic formula, shown below:
# root = −b ± √
# b2 − 4ac
# 2a
# The portion of the expression under the square root sign is called the discriminant.
# If the discriminant is negative then the quadratic equation does not have any real roots.
# If the discriminant is 0, then the equation has one real root. Otherwise the equation
# has two real roots, and the expression must be evaluated twice, once using a plus
# sign, and once using a minus sign, when computing the numerator.
# Write a program that computes the real roots of a quadratic function. Your program
# should begin by prompting the user for the values of a, b and c. Then it should display
# a message indicating the number of real roots, along with the values of the real roots
# (if any).

# solution:

import math


def compute_roots(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4 * a * c

    # Determine the number of roots and compute them
    if discriminant < 0:
        return 0, None, None  # No real roots
    elif discriminant == 0:
        root = -b / (2 * a)  # One real root
        return 1, root, None
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)  # Two real roots
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return 2, root1, root2


def main():
    while True:
        try:
            # Prompt the user for coefficients
            a = float(input("\nEnter the coefficient a: "))
            b = float(input("\nEnter the coefficient b: "))
            c = float(input("\nEnter the coefficient c: "))

            # Validate that a is not zero
            if a == 0:
                print(
                    "\nThe coefficient 'a' cannot be zero. Please enter a valid quadratic equation.")
                continue

            # Compute the roots
            num_roots, root1, root2 = compute_roots(a, b, c)

            # Display the results
            if num_roots == 0:
                print("\nThe quadratic equation has no real roots.")
            elif num_roots == 1:
                print(
                    f"\nThe quadratic equation has one real root: {root1:.2f}")
            else:
                print(
                    f"\nThe quadratic equation has two real roots: {root1:.2f} and {root2:.2f}")

            break  # Exit the loop after successful execution

        except ValueError:
            print("\nInvalid input. Please enter numeric values for the coefficients.")


if __name__ == "__main__":
    main()
