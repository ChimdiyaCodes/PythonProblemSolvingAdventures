# Exercise 151: Two Word Random Password

# While generating a password by selecting random characters generally gives a relatively secure password, it also generally gives a password that is difficult to memorize.
# As an alternative, some systems construct a password by taking two English words
# and concatenating them. While this password isn’t as secure, it is much easier to
# memorize.
# Write a program that reads a file containing a list of words, randomly selects two
# of them, and concatenates them to produce a new password. When producing the
# password ensure that the total length is between 8 and 10 characters, and that each
# word used is at least three letters long. Capitalize each word in the password so that
# the user can easily see where one word ends and the next one begins. Display the
# password for the user.

# solution

import random


def generate_password(word_list):
    """
    Tries to generate a password by randomly selecting two words from word_list
    such that:
    - Each word is at least 3 letters long
    - The total length of the concatenated two words is between 8 and 10 (inclusive)
    - Both words are capitalized before concatenation
    """

    filtered_words = []

    for word in word_list:
        if len(word) >= 3:
            filtered_words.append(word)

    if len(filtered_words) < 2:
        print(
            "Not enough words with at least 3 letters in the list to generate a password.")
        return None

    while True:
        word1 = random.choice(filtered_words)
        word2 = random.choice(filtered_words)

        # Avoid using the same word twice (optional)
        if word1 == word2:
            continue

        password = word1.capitalize() + word2.capitalize()
        total_length = len(password)

        if 8 <= total_length <= 10:
            return password


def main():
    input_filename = input(
        "Enter the name of the file containing words: ").strip()

    try:
        with open(input_filename, 'r') as file:
            words = [line.strip() for line in file if line.strip()]

        password = generate_password(words)

        if password:
            print(f"Generated password: {password}")
        else:
            print("Could not generate a valid password with the given word list.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
