# Exercise 69: Approximate π

# The value of π can be approximated by the following infinite series:
# π ≈ 3+
# 4
# 2 × 3 × 4 − 4
# 4 × 5 × 6 +
# 4
# 6 × 7 × 8 − 4
# 8 × 9 × 10 +
# 4
# 10 × 11 × 12 −···
# Write a program that displays 15 approximations of π. The first approximation
# should make use of only the first term from the infinite series. Each additional approximation displayed by your program should include one more term in the series, making
# it a better approximation of π than any of the approximations displayed previously.

# solution:

def approximate_pi():
    """
    Approximates the value of π using the given infinite series and displays 15 approximations.
    """
    # Initialize the approximation with the first term
    pi_approx = 3.0
    print(f"Approximation 1: {pi_approx}")

    # Initialize variables for the series
    n = 1  # Term counter
    sign = 1  # Alternates between +1 and -1 for addition/subtraction

    # Loop to calculate 15 approximations
    for i in range(2, 16):  # Start from 2 because the first term is already used
        # Calculate the denominator: (2n) * (2n+1) * (2n+2)
        denominator = (2 * n) * (2 * n + 1) * (2 * n + 2)

        # Calculate the current term: (4 / denominator) * sign
        term = (4 / denominator) * sign

        # Update the approximation of π
        pi_approx += term

        # Display the current approximation
        print(f"Approximation {i}: {pi_approx}")

        # Update variables for the next term
        sign *= -1  # Flip the sign for the next term
        n += 1  # Increment the term counter


# Run the function
approximate_pi()
