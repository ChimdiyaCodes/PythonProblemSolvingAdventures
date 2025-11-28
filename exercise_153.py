# Exercise 153: A Book with No “e”…

# The novel “Gadsby” is over 50,000 words in length. While 50,000 words isn’t normally remarkable for a novel, it is in this case because none of the words in the book
# use the letter “e”. This is particularly noteworthy when one considers that “e” is the
# most common letter in English.
# Write a program that reads a list of words from a file and determines what proportion of the words use each letter of the alphabet. Display the result for all 26
# letters. Include an additional message identifying the letter that is used in the smallest proportion of the words. Your program should ignore any punctuation marks and
# it should treat uppercase and lowercase letters as equivalent.

import string  # Contains all letters a-z

# Step 1: Ask user for file name
filename = input("Enter the name of the file: ")

try:
    with open(filename, "r") as file:
        # Step 2: Read all words into a list
        words = []
        for line in file:
            line = line.strip()  # Remove extra spaces or newlines
            if line:  # Only process non-empty lines
                # Remove punctuation & convert to lowercase
                # string.punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
                clean_line = line.translate(
                    str.maketrans("", "", string.punctuation))
                words.extend(clean_line.lower().split())  # Add words to list

except FileNotFoundError:
    print("File not found! Please check the filename.")
    exit()

# Step 3: Total number of words
total_words = len(words)
print(f"Total number of words: {total_words}")

# Step 4: Dictionary to store proportions
letter_proportions = {}

# Step 5: For each letter a-z, calculate proportion
for letter in string.ascii_lowercase:
    count = 0
    for word in words:
        if letter in word:
            count += 1  # Count how many words contain this letter

    proportion = count / total_words  # Calculate proportion
    letter_proportions[letter] = proportion

# Step 6: Display all results
print("\nProportion of words containing each letter:\n")
for letter, proportion in letter_proportions.items():
    print(f"{letter}: {proportion:.4f}")

# Step 7: Find letter with smallest proportion
smallest_letter = min(letter_proportions, key=letter_proportions.get)
print(
    f"\nThe letter used in the smallest proportion of words is: '{smallest_letter}'")
