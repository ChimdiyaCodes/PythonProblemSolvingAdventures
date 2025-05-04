# Exercise 92: Is a Number Prime?

# A prime number is an integer greater than 1 that is only divisible by one and itself.
# Write a function that determines whether or not its parameter is prime, returning
# True if it is, and False otherwise. Write a main program that reads an integer
# from the user and displays a message indicating whether or not it is prime. Ensure
# that the main program will not run if the file containing your solution is imported
# into another program.

# solution:

import math


def is_prime(number):
    """
    Determines if a number is prime.
    Returns True if n is a prime number, otherwise False.
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    # Check for factors from 3 up to √n
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def main():
    print("\n=== Your Prime Number Checker ===")
    print("Instruction: Enter a number to check if it's a prime number.")
    print("Type 'q' to quit.\n")

    while True:
        user_input = input("\nEnter an integer: ").strip()

        if user_input.lower() == 'q':
            print("Exiting... Goodbye!")
            break

        try:
            number = int(user_input)

            if is_prime(number):
                print(f"{number} is a prime number.\n")
            else:
                print(f"{number} is NOT a prime number.\n")

        except ValueError:
            print("Invalid input. Please enter a valid integer or 'q' to quit.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")


# Run only when the file is executed directly
if __name__ == "__main__":
    main()
