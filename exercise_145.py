# Exercise 145: Find the Longest Word in a File

# In this exercise you will create a Python program that identifies the longest word(s)
# in a file. Your program should output an appropriate message that includes the length
# of the longest word, along with all of the words of that length that occurred in the
# file. Treat any group of non-white space characters as a word, even if it includes
# numbers or punctuation marks.

# solution

# Ask the user for the filename
filename = input("Enter the filename: ")

try:
    # Open file using UTF-8 encoding (important!)
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    words = content.split()

    if not words:
        print("The file is empty or contains no words.")
        exit()

    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]

    print(f"\nLongest word length: {max_length}")
    print("Words with this length:")
    for word in set(longest_words):
        print(word)

except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")

except UnicodeDecodeError:
    print("⚠️ Unicode Error: This file contains characters Python cannot read with UTF-8.")
    print("Try saving the text file as UTF-8 encoding.")
