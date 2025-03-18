# Exercise 68: Parity Bits

# A parity bit is a simple mechanism for detecting errors in data transmitted over an
# unreliable connection such as a telephone line. The basic idea is that an additional bit
# is transmitted after each group of 8 bits so that a single bit error in the transmission
# can be detected.
# Parity bits can be computed for either even parity or odd parity. If even parity
# is selected then the parity bit that is transmitted is chosen so that the total number
# of one bits transmitted (8 bits of data plus the parity bit) is even. When odd parity
# is selected the parity bit is chosen so that the total number of one bits transmitted
# is odd.
# Write a program that computes the parity bit for groups of 8 bits entered by the
# user using even parity. Your program should read strings containing 8 bits until the
# user enters a blank line. After each string is entered by the user your program should
# display a clear message indicating whether the parity bit should be 0 or 1. Display
# an appropriate error message if the user enters something other than 8 bits.
# Hint: You should read the input from the user as a string. Then you can use
# the count method to help you determine the number of zeros and ones in the
# string. Information about the count method is available online.

# solution:

def compute_parity_bit(bits):
    # Count the number of 1s in the 8-bit string
    count_ones = bits.count('1')

    # Determine the parity bit based on even parity
    if count_ones % 2 == 0:
        return 0  # Even number of 1s, parity bit is 0
    else:
        return 1  # Odd number of 1s, parity bit is 1


def validate_input(bits):
    if len(bits) != 8:
        print("Error: Input must be exactly 8 bits long.")
        return False
    if not all(bit in '01' for bit in bits):
        print("Error: Input must contain only 0s and 1s.")
        return False
    return True


def main():
    """
    Main function to handle user input and compute parity bits.
    """
    while True:
        # Get input from the user
        bits = input("\nEnter 8 bits (or a blank line to quit): ").strip()

        # Exit if the user enters a blank line
        if bits == "":
            print("Exiting the program. Goodbye!")
            break

        # Validate the input
        if not validate_input(bits):
            continue  # Skip to the next iteration if input is invalid

        # Compute the parity bit
        parity_bit = compute_parity_bit(bits)

        # Display the result
        print(f"\nThe parity bit should be: {parity_bit}\n")


if __name__ == "__main__":
    main()
