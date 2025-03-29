# Exercise 77: Binary to Decimal

# Write a program that converts a binary (base 2) number to decimal (base 10). Your
# program should begin by reading the binary number from the user as a string. Then
# it should compute the equivalent decimal number by processing each digit in the
# binary number. Finally, your program should display the equivalent decimal number
# with an appropriate message.

# solution:

def binary_to_decimal():
    """
    Converts binary to decimal using Python's built-in int() function.
    Handles all input validation automatically through try-except.
    """
    while True:
        binary_str = input("\nEnter a binary number: ").strip()

        try:
            decimal = int(binary_str, 2)
            print(f"\nThe decimal equivalent of {binary_str} is: {decimal}")
            return decimal
        except ValueError:
            print("Error: Invalid binary number. Must contain only 0s and 1s.")


if __name__ == "__main__":
    binary_to_decimal()
