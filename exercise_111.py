# Exercise 111: Only the Words

# In this exercise you will create a program that identifies all of the words in a string
# entered by the user. Begin by writing a function that takes a string of text as its only
# parameter. Your function should return a list of the words in the string with the punctuation marks at the edges of the words removed. The punctuation marks that you must
# remove include commas, periods, question marks, hyphens, apostrophes, exclama￾tion points, colons, and semicolons. Do not remove punctuation marks that appear in
# the middle of a words, such as the apostrophes used to form a contraction. For example, if your function is provided with the string "Examples of contractions
# include: don’t, isn’t, and wouldn’t." then your function should
# return the list ["Examples", "of", "contractions", "include",
# "don’t", "isn’t", "and", "wouldn’t"].
# Write a main program that demonstrates your function. It should read a string
# from the user and display all of the words in the string with the punctuation marks
# removed. You will need to import your solution to this exercise when completing
# Exercise 158. As a result, you should ensure that your main program only runs when
# your file has not been imported into another program.

# solution

# Function to extract words from text and clean punctuation at word edges
def extract_words(text):
    # Define punctuation characters to strip from word edges
    punctuation = ",.?!-':;!"

    # Split the input into words
    raw_words = text.split()

    # Process each word
    cleaned_words = []
    for word in raw_words:
        # Strip only edge punctuation
        cleaned = word.strip(punctuation)
        cleaned_words.append(cleaned)

    return cleaned_words


# Function to safely get non-empty user input
def get_non_empty_input(prompt="\nEnter a sentence: "):
    while True:
        user_input = input(prompt).strip()
        if user_input == "":
            print("Input cannot be blank. Please enter a sentence.")
        else:
            return user_input


# Main program
def main():
    print("\n=== Word Cleaner ===")

    # Get validated sentence from user
    sentence = get_non_empty_input()

    # Extract cleaned words
    words = extract_words(sentence)

    # Display the result
    print("\nCleaned words:")
    for word in words:
        print(word)


# Run only when this file is executed directly
if __name__ == "__main__":
    main()
