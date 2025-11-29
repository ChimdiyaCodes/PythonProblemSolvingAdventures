# Exercise 164: Total the Values

# Write a program that reads values from the user until a blank line is entered. Display
# the total of all of the values entered by the user (or 0.0 if the first value entered is
# a blank line). Complete this task using recursion. Your program may not use any
# loops.
# Hint: The body of your recursive function will need to read one value from
# the user, and then determine whether or not to make a recursive call. Your
# function does not need to take any parameters, but it will need to return a
# numeric result.

# solution

def total_values():
    """
    Recursively read numeric values from user until blank line is entered.
    Return the sum of all entered values as a float.
    """
    user_input = input("Enter a value (blank to finish): ").strip()
    if user_input == "":
        # Base case: user entered blank line, stop recursion
        return 0.0
    else:
        # Convert input to float and add to sum from recursive call
        try:
            number = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number or blank to finish.")
            # Retry current call if input invalid
            return total_values()
        return number + total_values()


def main():
    print("This program sums values you enter.")
    total = total_values()
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
