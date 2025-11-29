# Exercise 168: Recursive Square Root

# Exercise 71 explored how iteration can be used to compute the square root of a
# number. In that exercise a better approximation of the square root was generated with
# each additional iteration of a loop. In this exercise you will use the same approximation strategy, but you will use recursion instead of iteration.
# Create a square root function that takes two parameters. The first parameter, n, will
# be the number for which the square root is being computed. The second parameter,
# guess, will be the current guess for the square root. The guess parameter should have
# a default value of 1.0. Do not provide a default value for the first parameter.
# Your square root function will be recursive. The base case occurs when guess2 is
# within 10−12 of n. In this case your function should return guess because it is close
# enough to the square root of n. Otherwise your function should return the result of
# calling itself recursively with n as the first parameter and guess+ guess
# n
# 2 as the second
# parameter.
# Write a main program that demonstrate your square root function by computing
# the square root of several different values. When you call your square root function
# from the main program you should only pass one parameter to it so that the default
# value for guess is used.

# solution
def recursive_sqrt(n, guess=1.0):
    """
    Recursively approximates the square root of n using Newton's method.
    Base case: when |guess^2 - n| < 1e-12
    Recursive case: improve the guess and call the function again.
    """
    # Base case
    if abs(guess * guess - n) < 1e-12:
        return guess

    # Compute new improved guess
    new_guess = (guess + n / guess) / 2

    # Recursive call
    return recursive_sqrt(n, new_guess)


def main():
    """
    Main program that demonstrates the recursive square root function.
    Includes input validation and error handling.
    """
    print("\nRecursive Square Root Calculator (Newton's Method)\n")

    while True:
        try:
            user_input = input(
                "Enter a positive number to compute its square root: ").strip()

            # Validate empty input
            if not user_input:
                print("Error: Input cannot be empty. Try again.")
                continue

            n = float(user_input)

            # Validate non-negative numbers
            if n < 0:
                print("Error: Square root of a negative number is not real. Try again.")
                continue

            # Call recursion (only pass n)
            result = recursive_sqrt(n)

            print(f"\nApproximate square root of {n} is: {result}")
            print(f"Python's math.sqrt({n}) gives:  {n ** 0.5}\n")

            break

        except ValueError:
            print("Error: Please enter a valid number.")
        except Exception as e:
            print(f"Unexpected error: {e}")


# Demonstrate for several values
def demo():
    print("\nDemonstration of recursive square root for several numbers:")
    test_values = [2, 9, 16, 0.25, 100, 0]

    for value in test_values:
        print(f"√{value} ≈ {recursive_sqrt(value)}")


if __name__ == "__main__":
    main()
    demo()
