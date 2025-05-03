# Exercise 89: Capitalize It

# Many people do not use capital letters correctly, especially when typing on small
# devices like smart phones. In this exercise, you will write a function that capitalizes
# the appropriate characters in a string. A lowercase “i” should be replaced with an
# uppercase “I” if it is both preceded and followed by a space. The first character in
# the string should also be capitalized, as well as the first non-space character after a
# “.”, “!” or “?”. For example, if the function is provided with the string “what time
# do i have to be there? what’s the address?” then it should return the string “What
# time do I have to be there? What’s the address?”. Include a main program that reads
# a string from the user, capitalizes it using your function, and displays the result.

# solution

def capitalize_properly(text):
    """
    Capitalizes the first character of the string, capitalizes 'i' when it's a standalone word,
    and capitalizes the first letter after '.', '!', or '?'.
    """
    result = ""
    capitalize_next = True  # True when we should capitalize the next letter

    i = 0
    while i < len(text):
        character = text[i]

        # Check for standalone "i"
        if character == 'i':
            # Check surrounding characteracters
            if (i == 0 or text[i - 1] == ' ') and (i + 1 == len(text) or text[i + 1] == ' '):
                result += 'I'
                i += 1
                continue

        # Capitalize first letter or after punctuation
        if capitalize_next and character.isalpha():
            result += character.upper()
            capitalize_next = False
        else:
            result += character

        # If current character is a punctuation that ends a sentence
        if character in ['.', '!', '?']:
            capitalize_next = True

        i += 1

    return result


def main():
    print("\nYour Proper Sentence Capitalizer")

    while True:
        try:
            user_input = input("\nEnter a sentence to capitalize: ").strip()

            if not user_input:
                raise ValueError(
                    "Input cannot be empty. Please enter a valid sentence.")

            formatted_text = capitalize_properly(user_input)
            print("\nHere's your formatted sentence:\n")
            print(formatted_text)
            break  # Exit loop after successful processing

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
