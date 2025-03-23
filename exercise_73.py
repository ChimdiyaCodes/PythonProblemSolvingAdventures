# Exercise 73: Multiple Word Palindromes

# There are numerous phrases that are palindromes when spacing is ignored. Examples
# include “go dog”, “flee to me remote elf” and “some men interpret nine memos”,
# among many others. Extend your solution to Exercise 72 so that it ignores spacing
# while determining whether or not a string is a palindrome. For an additional challenge,
# extend your solution so that is also ignores punctuation marks and treats uppercase
# and lowercase letters as equivalent.

# solution:

import string


def is_palindrome():
    while True:
        try:
            # Read input from the user
            word = input(
                "\nEnter a string to check if it is a palindrome: ").strip()

            # Validate input
            if not word:
                print("Error: Input cannot be empty. Please enter a valid string.")
                continue  # Restart the loop to get valid input

            # Convert to lowercase
            normal_word = word.lower()
            # Remove spaces and punctuation
            normal_word = normal_word.replace(" ", "")  # Remove spaces
            normal_word = normal_word.translate(str.maketrans(
                "", "", string.punctuation))  # Remove punctuation

            # Check if the string is a palindrome
            # Compare string with its reverse
            palindrome = normal_word == normal_word[::-1]

            # Output the result
            if palindrome:
                print(f'\n"{word}" is a palindrome!')
            else:
                print(f'\n"{word}" is not a palindrome.')

            break

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break


# Call the function to execute the program
is_palindrome()
