# Exercise 72: Is a String a Palindrome?

# A string is a palindrome if it is identical forward and backward. For example “anna”,
# “civic”, “level” and “hannah” are all examples of palindromic words.Write a program
# that reads a string from the user and uses a loop to determines whether or not it is a
# palindrome. Display the result, including a meaningful output message.

# solution

def is_palindrome():
    while True:
        try:
            # Read input from the user
            user_input = input(
                "\nEnter a word to check if it is a palindrome: ").strip()

            # Validate input
            if not user_input:
                print("Error: Input cannot be empty. Please enter a valid string.")
                continue

            # Normalize the string (optional, for case insensitivity and ignoring spaces
            normalized_input = user_input.lower().replace(" ", "")

            # Check if the string is a palindrome
            # Compare string with its reverse
            is_palindrome = normalized_input == normalized_input[::-1]

            # Output the result
            if is_palindrome:
                print(f'\n"{user_input}" is a palindrome!')
            else:
                print(f'\n"{user_input}" is not a palindrome.')

            break

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break


is_palindrome()
