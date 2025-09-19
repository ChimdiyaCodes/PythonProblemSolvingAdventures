# Exercise 127: The Sieve of Eratosthenes

# The Sieve of Eratosthenes is a technique that was developed more than 2,000 years
# ago to easily find all of the prime numbers between 2 and some limit, say 100. A
# description of the algorithm follows:
# Write down all of the numbers from 0 to the limit
# Cross out 0 and 1 because they are not prime
# Set p equal to 2
# While p is less than the limit do
# Cross out all multiples of p (but not p itself)
# Set p equal to the next number in the list that is not crossed out
# Report all of the numbers that have not been crossed out as prime
# The key to this algorithm is that it is relatively easy to cross out every nth number
# on a piece of paper. This is also an easy task for a computer—a for loop can simulate
# this behavior when a third parameter is provided to the range function. When a
# number is crossed out, we know that it is no longer prime, but it still occupies space on
# the piece of paper, and must still be considered when computing later prime numbers.
# This copy belongs to 'acha04'
# 60 5 List Exercises
# As a result, you should not simulate crossing out a number by removing it from the
# list. Instead, you should simulate crossing out a number by replacing it with 0. Then,
# once the algorithm completes, all of the non-zero values in the list are prime.
# Create a Python program that uses this algorithm to display all of the prime
# numbers between 2 and a limit entered by the user. If you implement the algorithm
# correctly you should be able to display all of the prime numbers less than 1,000,000
# in a few seconds.
# This algorithm for finding prime numbers is not Eratosthenes’ only claim to
# fame. His other noteworthy accomplishments include calculating the circumference of the Earth and the tilt of the Earth’s axis. He also served as the Chief
# Librarian at the Library of Alexandria.

def sieve_of_eratosthenes(limit):
    # Step 1: Create list of numbers from 0 to limit
    numbers = list(range(limit + 1))

    # Step 2: Cross out 0 and 1
    numbers[0] = 0
    numbers[1] = 0

    # Step 3: Start with first prime, p = 2
    p = 2
    while p <= limit:
        if numbers[p] != 0:  # If p is not crossed out
            # Step 4: Cross out multiples of p
            for multiple in range(p * 2, limit + 1, p):
                numbers[multiple] = 0
        p += 1  # Move to the next number

    # Step 5: Extract primes (non-zero values)
    primes = [num for num in numbers if num != 0]
    return primes


# --- Main Program ---
if __name__ == "__main__":
    print("\nThis program takes a number from you as upper limit and prints "
          "all the prime numbers that come before it.")
    limit = int(input("\nEnter the upper limit: "))
    primes = sieve_of_eratosthenes(limit)
    print(f"\nPrime numbers up to {limit} are:")
    print(primes)
