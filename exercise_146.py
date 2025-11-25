# Exercise 146: Letter Frequencies

# One technique that can be used to help break some simple forms of encryption is
# frequency analysis. This analysis examines the encrypted text to determine which
# characters are most common. Then it tries to map the most common letters in English, such as E and T, to the most commonly occurring characters in the encrypted
# text.
# Write a program that initiates this process by determining and displaying the
# frequencies of all letters in a file. Ignore spaces, punctuation marks, and numbers as
# you perform this analysis. Your program should be case insensitive, treating a and
# A as equivalent. The user will provide the file name as a command line parameter.
# Your program should display a meaningful error message if the user provides the
# wrong number of command line parameters, or if the program is unable to open the
# file indicated by the user.

# solution

import sys
from collections import Counter


def count_letter_frequencies(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read().lower()

        letters_only = ""
        for char in text:
            if char.isalpha():  # Keep only letters A-Z
                letters_only += char

        frequencies = Counter(letters_only)

        if not frequencies:
            print("No letters found in this file.")
            return

        print("Letter Frequencies:\n")
        for letter, freq in sorted(frequencies.items()):
            print(f"{letter}: {freq}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to open '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    if len(sys.argv) != 2:  # Must provide EXACTLY one filename
        print("Usage: python exercise_146.py <filename>")
        return

    filename = sys.argv[1]
    count_letter_frequencies(filename)


if __name__ == "__main__":
    main()
