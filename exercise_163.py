# Exercise 163:Words with Six Vowels in Order

# There is at least one word in the English language that contains each of the vowels
# a, e, i, o, u and y exactly once and in order. Write a program that searches a file
# containing a list of words and displays all of the words that meet this constraint. The
# user will provide the name of the file that will be searched. Display an appropriate
# error message and exit the program if the user provides an invalid file name or if
# something else goes wrong while searching for words with six vowels in order.

# solution

"""

Usage:
    python six_vowels.py wordlist.txt
"""

import sys
import re

TARGET_VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']


def normalize_word(raw):
    """
    Convert to lowercase and remove any non-letter characters.
    Returns the cleaned word (only letters a-z).
    """
    if raw is None:
        return ""
    w = raw.strip().lower()
    # remove anything that is not a lowercase ASCII letter
    w = re.sub(r'[^a-z]', '', w)
    return w


def has_six_vowels_once_in_order(word):
    """
    Return True if 'word' contains each vowel in TARGET_VOWELS exactly once
    and in the same order (positions strictly increasing).
    """
    # quick reject: word must contain at least 6 letters
    if len(word) < 6:
        return False

    positions = []
    for v in TARGET_VOWELS:
        count = word.count(v)
        if count != 1:
            return False   # must appear exactly once
        pos = word.find(v)
        positions.append(pos)

    # ensure positions are strictly increasing (a before e before i ...)
    for earlier, later in zip(positions, positions[1:]):
        if earlier >= later:
            return False

    return True


def find_matching_words(filename):
    """
    Read filename and yield words that meet the vowel constraint.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for raw_line in f:
                if not raw_line:
                    continue
                cleaned = normalize_word(raw_line)
                if not cleaned:
                    continue
                if has_six_vowels_once_in_order(cleaned):
                    yield cleaned
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return
    except Exception as e:
        print(f"Error while processing {filename}: {e}")
        return


def main():
    if len(sys.argv) != 2:
        print("Usage: python six_vowels.py wordlist.txt")
        return

    filename = sys.argv[1]
    any_found = False

    for word in find_matching_words(filename):
        if not any_found:
            print("Words that contain a, e, i, o, u, y exactly once and in order:")
            any_found = True
        print(word)

    if not any_found:
        print("No matching words found.")


if __name__ == "__main__":
    main()
