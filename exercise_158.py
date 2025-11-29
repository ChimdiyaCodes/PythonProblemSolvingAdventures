# Exercise 158: Spell Checker

# A spell checker can be a helpful tool for people who struggle to spell words correctly.
# In this exercise, you will write a program that reads a file and displays all of the words
# in it that are misspelled. Misspelled words will be identified by checking each word
# in the file against a list of known words. Any words in the user’s file that do not
# appear in the list of known words will be reported as spelling mistakes.
# The user will provide the name of the file to check for spelling mistakes as a
# command line parameter. Your program should display an appropriate error message
# if the command line parameter is missing. An error message should also be displayed
# if your program is unable to open the user’s file. Use your solution to Exercise 111
# when creating your solution to this exercise so that words followed by a comma,
# period or other punctuation mark are not reported as spelling mistakes. Ignore the
# capitalization of the words when checking their spelling.
# Hint: While you could load all of the English words from the words data set
# into a list, searching a list is slow if you use Python’s in operator. It is much
# faster to check if a key is present in a dictionary, or if a value is present in a
# set. If you use a dictionary, the words will be the keys. The values can be the
# integer 0 (or any other value) because the values will never be used.

import sys

# Import your extract_words function from Exercise 111
from exercise_111 import extract_words


def load_dictionary(dictionary_file):
    """Load all known English words into a set for fast lookup."""
    try:
        with open(dictionary_file, "r") as file:
            words = set()
            for line in file:
                words.add(line.strip().lower())  # remove newline + lowercase
            return words
    except:
        print(f"Error: Could not open dictionary file '{dictionary_file}'.")
        return None


def main():
    # 1. Check for command line argument
    if len(sys.argv) < 2:
        print("Error: You must provide a filename to check.")
        print("Usage: python spell_checker.py user_file.txt")
        return

    filename = sys.argv[1]

    # 2. Try to open user’s file
    try:
        with open(filename, "r") as user_file:
            lines = user_file.readlines()
    except:
        print(f"Error: Could not open the file '{filename}'.")
        return

    # 3. Load dictionary words
    dictionary = load_dictionary("words.txt")  # You must have this file!
    if dictionary is None:
        return  # Stop if dictionary failed to load

    # 4. Find misspelled words
    misspelled = set()

    for line in lines:
        words = extract_words(line)  # From Exercise 111

        for word in words:
            clean_word = word.lower()
            if clean_word not in dictionary and clean_word != "":
                misspelled.add(clean_word)

    # 5. Output results
    if len(misspelled) == 0:
        print("No spelling mistakes found! ✔")
    else:
        print("\nMisspelled words:")
        for word in sorted(misspelled):  # Sorted for neat output
            print(word)


if __name__ == "__main__":
    main()
