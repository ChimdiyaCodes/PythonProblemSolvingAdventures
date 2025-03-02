# Exercise 45: What Color is that Square?

# Positions on a chess board are identified by a letter and a number. The letter identifies
# the column, while the number identifies the row, as shown below:
# 1 a
# 2 b
# 3 c
# 4 d
# 5 e
# 6 f
# 7 g
# 8 h

# Write a program that reads a position from the user. Use an if statement to determine if the column begins with a black square or a white square. Then use modular
# arithmetic to report the color of the square in that row. For example, if the user enters
# a1 then your program should report that the square is black. If the user enters d5
# then your program should report that the square is white. Your program may assume
# that a valid position will always be entered. It does not need to perform any error
# checking.

# solution

def get_square_color(position):
    # Check if the input is exactly 2 characters long
    if len(position) != 2:
        raise ValueError(
            "Invalid input: Position must be exactly 2 characters long (e.g., a1, d5).")

    # Extract the column letter and row number
    # Convert to lowercase to handle uppercase inputs
    column_letter = position[0].lower()
    row_char = position[1]

    # Validate the column letter (must be between 'a' and 'h')
    if column_letter < 'a' or column_letter > 'h':
        raise ValueError(
            "Invalid input: Column must be a letter from 'a' to 'h'.")

    # Validate the row number (must be a digit between 1 and 8)
    if not row_char.isdigit():
        raise ValueError("Invalid input: Row must be a number from 1 to 8.")
    row_number = int(row_char)
    if row_number < 1 or row_number > 8:
        raise ValueError("Invalid input: Row must be a number from 1 to 8.")

    # Map the column letter to a number (a=1, b=2, ..., h=8)
    column_number = ord(column_letter) - ord('a') + 1

    # Calculate the sum of the column number and row number
    total = column_number + row_number

    # Determine the color of the square
    if total % 2 == 0:
        color = "white"
    else:
        color = "black"

    return color


# Main program
while True:
    try:
        # Read the position from the user
        position = input("Enter the position (e.g., a1, d5, h8): ")

        # Get the color of the square
        color = get_square_color(position)

        # Output the result
        print(f"The square {position} is {color}.")
        break  # Exit the loop if the input is valid
    except ValueError as e:
        print(f"Error: {e}")
        print("Please try again.\n")
