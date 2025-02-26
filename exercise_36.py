# Exercise 36:Vowel or Consonant

# In this exercise you will create a program that reads a letter of the alphabet from the
# user. If the user enters a, e, i, o or u then your program should display a message
# indicating that the entered letter is a vowel. If the user enters y then your program
# should display a message indicating that sometimes y is a vowel, and sometimes y is
# a consonant. Otherwise your program should display a message indicating that the
# letter is a consonant.

# solution

def classify_letter(letter):
    # Convert the letter to lowercase to handle case insensitivity
    letter = letter.lower()

    # Check if the input is a single character and a valid letter
    if len(letter) != 1 or not letter.isalpha():
        return "Error: Please enter a single valid letter of the alphabet."

    # Classify the letter
    if letter in ['a', 'e', 'i', 'o', 'u']:
        return f"\nThe letter {letter} is a vowel."
    elif letter == 'y':
        return "\nThe letter y is sometimes a vowel and sometimes a consonant."
    else:
        return f"\nThe letter {letter} is a consonant."

# Main program


def main():
    while True:  # Keep running until a valid input is provided
        # Take input from the user
        user_input = input("\nEnter a single letter of the alphabet: ")

        # Classify the letter and get the result
        result = classify_letter(user_input)

        # Display the result
        print(result)

        # Check if the result is an error message
        if not result.startswith("Error"):
            break  # Exit the loop if the input was valid


# Run the program
if __name__ == "__main__":
    main()
