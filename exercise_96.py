# Exercise 96: Check a Password

# In this exercise you will write a function that determines whether or not a password
# is good. We will define a good password to be a one that is at least 8 characters
# long and contains at least one uppercase letter, at least one lowercase letter, and at
# least one number. Your function should return true if the password passed to it as
# its only parameter is good. Otherwise it should return false. Include a main program
# that reads a password from the user and reports whether or not it is good. Ensure

# that your main program only runs when your solution has not been imported into
# another file.

# solution

def good_password(password):
    # Check length
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter
    upper_character = any(character.isupper() for character in password)

    # Check for at least one lowercase letter
    lower_character = any(character.islower() for character in password)
    # Check for at least one digit
    digit = any(character.isdigit() for character in password)

    # Return True only if all conditions are met
    return upper_character and lower_character and digit


def main():
    print("\n-----Good Password Checker------")
    print("This program checks if your password is good. It must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, and one number.")
    password = input("\nEnter your password: ")
    if good_password(password):
        print("\nYour password is good.")
    else:
        print("\nYour password is not good. It must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, and one number.")


# Make sure the main function only runs if the file is executed directly
if __name__ == "__main__":
    main()
