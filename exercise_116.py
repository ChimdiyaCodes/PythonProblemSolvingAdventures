# Exercise 116: Pig Latin Improved
# (51 Lines)
# Extend your solution to Exercise 115 so that it correctly handles uppercase letters and
# punctuation marks such as commas, periods, question marks and exclamation marks.
# If an English word begins with an uppercase letter then its Pig Latin representation
# should also begin with an uppercase letter and the uppercase letter moved to the end of
# the word should be changed to lowercase. For example, Computer should become
# Omputercay. If a word ends in a punctuation mark then the punctuation mark
# should remain at the end of the word after the transformation has been performed.
# For example, Science! should become Iencescay!.

# solution

import string


def is_valid_input(sentence):
    # Valid: lowercase, uppercase, space, punctuation (.,!?)
    allowed = string.ascii_letters + string.whitespace + ".,!?"
    return all(char in allowed for char in sentence)


def pig_latin_word(word):
    vowels = "aeiou"
    punctuation = ""

    # Check for ending punctuation
    if word and word[-1] in ".,!?":
        punctuation = word[-1]
        word = word[:-1]

    # Check if first letter was uppercase
    was_upper = word[0].isupper() if word else False

    # Lowercase the word for processing
    word_lower = word.lower()

    # Pig Latin logic
    if word_lower[0] in vowels:
        result = word_lower + "way"
    else:
        for index, letter in enumerate(word_lower):
            if letter in vowels:
                result = word_lower[index:] + word_lower[:index] + "ay"
                break
        else:
            result = word_lower + "ay"

    # Restore capitalization
    if was_upper:
        result = result.capitalize()

    # Add punctuation back
    return result + punctuation


def pig_latin_sentence(sentence):
    words = sentence.split()
    translated_words = []

    for word in words:
        translated = pig_latin_word(word)
        translated_words.append(translated)

    return ' '.join(translated_words)


# Main loop with validation and error handling
while True:
    try:
        user_input = input(
            "\nEnter a sentence (letters, spaces, .,!?): ").strip()

        if not user_input:
            print("Input cannot be empty. Please try again.\n")
            continue

        if not is_valid_input(user_input):
            print(
                "Invalid input. Only letters, spaces, and . , ! ? are allowed. Please try again.\n")
            continue

        result = pig_latin_sentence(user_input)
        print("\nPig Latin translation:", result)
        break

    except Exception as e:
        print(f"An error occurred: {e}. Please try again.\n")
