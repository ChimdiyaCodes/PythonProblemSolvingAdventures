# Exercise 109: List of Proper Divisors

# A proper divisor of a positive integer, n, is a positive integer less than n which divides
# evenly into n. Write a function that computes all of the proper divisors of a positive
# integer. The integer will be passed to the function as its only parameter. The function
# will return a list containing all of the proper divisors as its only result. Complete
# this exercise by writing a main program that demonstrates the function by reading
# a value from the user and displaying the list of its proper divisors. Ensure that your
# main program only runs when your solution has not been imported into another file.

# solution:

# Function to return proper divisors of a positive integer n
def proper_divisors(n):
    # Initialize an empty list to store the divisors
    divisors = []

    for i in range(1, n):
        # If i divides n evenly, it's a proper divisor
        if n % i == 0:
            divisors.append(i)

    # Return the list of proper divisors
    return divisors


# Function to prompt the user and validate input
def get_positive_integer():
    while True:
        user_input = input("\nEnter a positive integer: ")

        if user_input == "":
            print("Input cannot be blank. Please enter a positive integer.")
            continue

        try:
            # Try to convert the input to an integer
            value = int(user_input)

            # Ensure the number is greater than 0
            if value <= 0:
                print("Please enter a number greater than 0.")
            else:
                return value
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a valid positive integer.")


# Main function
def main():
    # Get a valid number from the user
    number = get_positive_integer()

    # Get the list of proper divisors
    divisors = proper_divisors(number)

    # Display the results
    print(f"\nProper divisors of {number} are:")
    for divisor in divisors:
        print(divisor)


if __name__ == "__main__":
    main()
