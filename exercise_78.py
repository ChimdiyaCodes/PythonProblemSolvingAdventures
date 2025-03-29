# Exercise 78: Decimal to Binary

# Write a program that converts a decimal (base 10) number to binary (base 2). Read the
# decimal number from the user as an integer and then use the division algorithm shown
# below to perform the conversion. When the algorithm completes, result contains the
# binary representation of the number. Display the result, along with an appropriate
# message.
# Let result be an empty string
# Let q represent the number to convert
# repeat
# Set r equal to the remainder when q is divided by 2
# Convert r to a string and add it to the beginning of result
# Divide q by 2, discarding any remainder, and store the result back into q
# until q is 0

# solution

def decimal_to_binary():
    """
    Converts a decimal number to binary using the division algorithm.
    Includes comprehensive input validation and error handling.
    """
    while True:
        try:
            # Get user input
            decimal_str = input("\nEnter a decimal number: ").strip()

            # Check for empty input
            if not decimal_str:
                print("Error: Input cannot be empty. Please try again.")
                continue

            # Convert to integer
            decimal = int(decimal_str)

            # Handle special case for 0
            if decimal == 0:
                print("The binary equivalent of 0 is: 0")
                return "0"

            # Store original for output
            original = decimal

            # Work with positive numbers
            is_negative = False
            if decimal < 0:
                is_negative = True
                decimal = abs(decimal)

            # Conversion algorithm
            result = ""
            q = decimal

            while q > 0:
                r = q % 2  # Get remainder
                result = str(r) + result  # Prepend to result
                q = q // 2  # Integer division

            # Add negative sign if needed
            if is_negative:
                result = "-" + result

            print(f"\nThe binary equivalent of {original} is: {result}")
            return result

        except ValueError:
            print("Error: Please enter a valid integer.")


# Run the program
if __name__ == "__main__":
    decimal_to_binary()
