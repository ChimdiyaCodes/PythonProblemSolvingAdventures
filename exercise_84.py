# Exercise 84: Median of Three Values

# Write a function that takes three numbers as parameters, and returns the median value
# of those parameters as its result. Include a main program that reads three values from
# the user and displays their median.
# Hint: The median value is the middle of the three values when they are sorted
# into ascending order. It can be found using if statements, or with a little bit of
# mathematical creativity

# solution:

def median_of_three(a, b, c):
    """
    Returns the median of three numbers.
    """
    numbers = [a, b, c]
    numbers.sort()
    return numbers[1]  # Middle value after sorting


def get_valid_number(prompt):
    """
    Repeatedly prompts the user for input until a valid float is entered.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("\nYou will be asked to enter three numbers to get their median:")

    # Input collection with validation
    num1 = get_valid_number("\nEnter the first number: ")
    num2 = get_valid_number("Enter the second number: ")
    num3 = get_valid_number("Enter the third number: ")

    # Call function and display result
    result = median_of_three(num1, num2, num3)
    print(f"\nThe median of {num1}, {num2}, and {num3} is: {result}")


# Run the program
if __name__ == "__main__":
    main()
