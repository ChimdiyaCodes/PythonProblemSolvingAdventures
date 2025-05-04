# Exercise 90: Does a String Represent an Integer?

# In this exercise you will write a function named isInteger that determines
# whether or not the characters in a string represent a valid integer. When determining
# if a string represents an integer you should ignore any leading or trailing white space.
# Once this white space is ignored, a string represents an integer if its length is at least
# 1 and it only contains digits, or if its first character is either + or - and the first
# character is followed by one or more characters, all of which are digits.
# Write a main program that reads a string from the user and reports whether or
# not it represents an integer. Ensure that the main program will not run if the file
# containing your solution is imported into another program.

def isInteger(string):
    # Step 1: Strip leading/trailing whitespace
    string = string.strip()

    # Step 2: Return False if string is empty
    if len(string) == 0:
        return False

    # Step 3: Check for optional + or - sign
    if string[0] in ('+', '-'):
        # Must be followed by at least one digit
        if len(string) == 1:
            return False
        return string[1:].isdigit()

    # Step 4: If no sign, all characters must be digits
    return string.isdigit()

# Main program


def main():
    user_input = input("\nEnter a string to check if it's an integer: ")
    if isInteger(user_input):
        print("\nThe string represents an integer.")
    else:
        print("\nThe string does not represent an integer.")


# Ensure main only runs when script is executed directly
if __name__ == "__main__":
    main()
