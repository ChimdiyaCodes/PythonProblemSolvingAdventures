# Importing the isPrime function from Exercise 92
from math import sqrt


def isPrime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def nextPrime(n):
    """Find the next prime number greater than n."""
    # Start with the next number after n
    next_number = n + 1

    # Loop until we find a prime number
    while True:
        if isPrime(next_number):  # Check if it's prime
            return next_number
        next_number += 1  # If not, try the next number


# Main program logic
if __name__ == "__main__":
    while True:
        try:
            # Ask the user to enter a number
            user_input = input(
                "\nEnter an integer to find the next prime number: ")
            n = int(user_input)

            # Find and display the next prime
            next_prime = nextPrime(n)
            print(f"\nThe next prime number after {n} is {next_prime}.")
            break  # Exit the loop if everything went well

        except ValueError:
            print("Invalid input! Please enter a valid integer.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
