# Exercise 107: Avoiding Duplicates

# In this exercise, you will create a program that reads words from the user until the
# user enters a blank line. After the user enters a blank line your program should display each word entered by the user exactly once. The words should be displayed in
# the same order that they were entered. For example, if the user enters:
# first
# second
# first
# third
# second
# then your program should display:
# first
# second
# third

# solution:

# Initialize storage structures
words = []  # To store words in order
seen = set()    # To store already entered words (for duplicate checking)

while True:
    word = input("\nEnter a word (blank to finish): ")

    if word == "":
        break

    if word not in seen:
        seen.add(word)
        words.append(word)

# Display the unique words in order

print("\nWords entered (without duplicates): ")
for word in words:
    print(word)
