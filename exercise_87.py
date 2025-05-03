# Exercise 87: Center a String in the Terminal
# Write a function that takes a string of characters as its first parameter, and the width of
# the terminal in characters as its second parameter. Your function should return a new
# string that consists of the original string and the correct number of leading spaces
# so that the original string will appear centered within the provided width when it is
# printed. Do not add any characters to the end of the string. Include a main program
# that demonstrates your function.

# solution

def center_string(text, width):

    spaces = (width - len(text)) // 2
    return ' ' * spaces + text


def main():
    while True:
        try:
            text = input("\nEnter the string to center: ").strip()
            if not text:
                raise ValueError("The string cannot be empty.")

            width_input = input(
                "Enter the width of the terminal (positive integer): ").strip()
            width = int(width_input)
            if width < len(text):
                raise ValueError(
                    "The terminal width must be at least as long as the string.")

            # If inputs are valid, break the loop
            break

        except ValueError as e:
            print(f"Input error: {e}. Please try again.")

    # Call the function and display result
    centered = center_string(text, width)
    print("\nYour Centered Output is:")
    print(centered)


# Run the main program
if __name__ == "__main__":
    main()
