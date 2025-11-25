# Exercise 147:Words that Occur Most

# Write a program that displays the word (or words) that occur most frequently in a
# file. Your program should begin by reading the name of the file from the user. Then
# it should find the word(s) by splitting each line in the file at each space. Finally,
# any leading or trailing punctuation marks should be removed from each word. In
# addition, your program should ignore capitalization. As a result, apple, apple!,
# Apple and ApPlE should all be treated as the same word. You will probably find
# your solution to Exercise 111 helpful when completing this problem.

# solution

import string


def get_most_frequent_words(filename):
    try:
        word_counts = {}

        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                for word in words:
                    # Remove leading/trailing punctuation
                    cleaned_word = word.strip(string.punctuation).lower()
                    if cleaned_word:  # ignore empty strings
                        word_counts[cleaned_word] = word_counts.get(
                            cleaned_word, 0) + 1

        if not word_counts:
            print("The file is empty or contains no valid words.")
            return

        max_count = max(word_counts.values())
        most_frequent_words = [
            word for word, count in word_counts.items() if count == max_count]

        print(f"The most frequent word(s) occurred {max_count} times:")
        for word in most_frequent_words:
            print(word)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to open '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    filename = input("Enter the filename: ")
    get_most_frequent_words(filename)


if __name__ == "__main__":
    main()
