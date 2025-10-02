# Exercise 130: Text Messaging

# On some basic cell phones, text messages can be sent using the numeric keypad.
# Because each key has multiple letters associated with it, multiple key presses are
# needed for most letters. Pressing the number once generates the first letter on the
# key. Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth or fifth
# character listed for that key.
# Key Symbols
# 1 .,?!:
# 2 ABC
# 3 DEF
# 4 GHI
# 5 JKL
# 6 MNO
# 7 PQRS
# 8 TUV
# 9 WXYZ
# 0 space
# Write a program that displays the key presses that must be made to enter a text
# message read from the user. Construct a dictionary that maps from each letter or
# symbol to the key presses. Then use the dictionary to generate and display the presses
# for the user’s message. For example, if the user enters Hello, World! then your
# program should output 4433555555666110966677755531111. Ensure that
# your program handles both uppercase and lowercase letters. Ignore any characters
# that aren’t listed in the table above such as semicolons and brackets.

# solution:

def build_keypad_mapping():
    """Builds a dictionary that maps characters to keypad presses."""
    keypad = {
        "1": ".,?!:",
        "2": "ABC",
        "3": "DEF",
        "4": "GHI",
        "5": "JKL",
        "6": "MNO",
        "7": "PQRS",
        "8": "TUV",
        "9": "WXYZ",
        "0": " "
    }

    mapping = {}
    for key, chars in keypad.items():
        for i, char in enumerate(chars):
            mapping[char] = key * (i + 1)  # e.g. 'C' → '222'
    return mapping


def text_to_keypress(message, mapping):
    """Converts a message into keypad presses using the mapping."""
    result = ""
    for char in message.upper():
        if char in mapping:
            result += mapping[char]
        # ignore unknown characters
    return result


def main():
    mapping = build_keypad_mapping()

    while True:
        try:
            message = input(
                "\nEnter your text message (or type 'quit' to exit): ").strip()
            if message.lower() == "quit":
                print("\nExiting program. Goodbye!")
                break

            if not message:
                raise ValueError("Empty message. Please enter some text.")

            keypresses = text_to_keypress(message, mapping)

            # using f-string here
            print(f"\nMessage: {message}")
            print(f"\nKey presses needed: {keypresses}")

        except Exception as e:
            print(f"Error: {e}. Please try again.")


if __name__ == "__main__":
    main()
