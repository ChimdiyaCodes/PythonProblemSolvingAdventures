# Exercise 148: Sum a List of Numbers

# Create a program that sums all of the numbers entered by the user while ignoring
# any lines entered by the user that are not valid numbers. Your program should display the current sum after each number is entered. It should display an appropriate
# error message after any invalid input, and then continue to sum any additional numbers entered by the user. Your program should exit when the user enters a blank
# line. Ensure that your program works correctly for both integers and floating point
# numbers.
# Hint: This exercise requires you to use exceptions without using files.

# solution

total = 0.0  # Running total (starts at zero)

print("Enter numbers to sum them. Press Enter on a blank line to finish.\n")

while True:
    user_input = input("Enter a number (or press Enter to exit): ")

    # Exit condition
    if user_input == "":
        print("\nProgram ended.")
        print(f"Final sum = {total}")
        break

    try:
        # Try converting to a float (handles both int & decimal numbers)
        number = float(user_input)
        total += number
        print(f"Current sum: {total}")  # Display running total

    except ValueError:
        # Error message for invalid input
        print("❌ Invalid input. Please enter a valid number.")
