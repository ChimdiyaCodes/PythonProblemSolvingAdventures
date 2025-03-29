# Exercise 76: Prime Factors

# The prime factorization of an integer, n, can be determined using the following steps:
# Initialize factor to two
# While factor is less than or equal to n do
# If n is evenly divisible by factor then
# Conclude that factor is a factor of n
# Divide n by factor using integer division
# Else
# Increase factor by one
# Write a program that reads an integer from the user. If the value entered by the
# user is less than 2 then your program should display an appropriate error message.
# Otherwise your program should display the prime numbers that can be multiplied
# together to compute n, with one factor appearing on each line. For example:
# Enter an integer (2 or greater):
# The prime factors of 72 are:
# 2 2 2 3 3

def get_prime_factors():
    """
    This function gets an integer input from the user (≥2) and displays its prime factors.
    Handles input validation and error management.
    """
    while True:
        try:
            # Get user input
            n = int(input("\nEnter an integer (2 or greater): "))

            # Input validation
            if n < 2:
                print("Error: Input must be 2 or greater. Please try again.")
                continue

            break  # Exit loop if input is valid

        except ValueError:
            print("Error: Please enter a valid integer.")

    original_n = n
    factors = []
    factor = 2  # Start with the smallest prime

    print(f"\nThe prime factors of {original_n} are: ")

    while factor <= n:
        if n % factor == 0:
            # Factor is a prime factor
            print(factor)
            factors.append(factor)
            n = n // factor
        else:
            factor += 1

    return factors


# Call the function
if __name__ == "__main__":
    prime_factors = get_prime_factors()
