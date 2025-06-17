# Exercise 115: Pig Latin

# Pig Latin is a language constructed by transforming English words. While the origins of the language are unknown, it is mentioned in at least two documents from
# the nineteenth century, suggesting that it has existed for more than 100 years. The
# following rules are used to translate English into Pig Latin:
# • If the word begins with a consonant (including y), then all letters at the beginning of
# the word, up to the first vowel (excluding y), are removed and then added to the end
# of the word, followed by ay. For example, computer becomes omputercay
# and think becomes inkthay.
# • If the word begins with a vowel (not including y), then way is added to the end
# of the word. For example, algorithm becomes algorithmway and office
# becomes officeway.
# Write a program that reads a line of text from the user. Then your program should
# translate the line into Pig Latin and display the result. You may assume that the string
# entered by the user only contains lowercase letters and spaces.

# solution

def is_valid_input(text):
    # Checks if input contains only lowercase letters and spaces
    for char in text:
        if not (char.islower() or char == ' '):
            return False
    return True


def pig_latin_word(word):
    vowels = 'aeiou'

    if word[0] in vowels:
        # Rule: word starts with vowel
        return word + 'way'
    else:
        # Rule: word starts with consonant
        # Find the position of the first vowel
        for index, letter in enumerate(word):
            if letter in vowels:
                # Move prefix to end and add 'ay'
                return word[index:] + word[:index] + 'ay'
        # If no vowel found (just in case), treat whole word as consonant
        return word + 'ay'


def pig_latin_sentence(sentence):
    words = sentence.split()
    translated_words = [pig_latin_word(word) for word in words]
    return ' '.join(translated_words)


# Main program loop
while True:
    try:
        user_input = input(
            "\nEnter a line of text (only lowercase letters and spaces): ").strip()

        if not user_input:
            print("Input cannot be empty. Please try again.\n")
            continue

        if not is_valid_input(user_input):
            print(
                "Invalid input. Only lowercase letters and spaces are allowed. Please try again.\n")
            continue

        # Translate and print the Pig Latin version
        result = pig_latin_sentence(user_input)
        print("Pig Latin translation:", result)
        break

    except Exception as e:
        print(f"An error occurred: {e}. Please try again.\n")
