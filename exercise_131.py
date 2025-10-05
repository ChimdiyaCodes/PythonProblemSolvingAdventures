# Exercise 131: Morse Code

# Morse code is an encoding scheme that uses dashes and dots to represent numbers
# and letters. In this exercise, you will write a program that uses a dictionary to store
# the mapping from letters and numbers to Morse code. Use a period to represent a dot,
# and a hyphen to represent a dash. The mapping from letters and numbers to dashes
# and dots is shown in Table 6.1.
# Your program should read a message from the user. Then it should translate each
# letter and number in the message to Morse code, leaving a space between each
# sequence of dashes and dots. Your program should ignore any characters that are not
# letters or numbers. The Morse code for Hello, World! is shown below:
# .... . .-.. .-.. --- .-- --- .-. .-.. -..
# Table 6.1 Morse Code Letters and Numbers
# Letter Code Letter Code Letter Code Number Code
# A .- J .- - - S ... 1 .- - - -
# B -... K -.- T - 2 ..- - -
# C -.-. L .-.. U ..- 3 ...- -
# D -.. M - - V ...- 4 ....-
# E . N -. W .- - 5 .....
# F ..-. O --- X -..- 6 -....
# G - -. P .- -. Y -.- - 7 - -...
# H .... Q - -.- Z - -.. 8 - - -..
# I .. R .-. 0 ----- 9 - - - -.

# Morse code was originally developed in the nineteenth century for use over
# telegraph wires. It is still used today, over 160 years after it was first created.

# solution:

# Morse Code Translator with Input Validation

# Step 1: Dictionary of Morse Code
MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}


def text_to_morse(text):
    # Convert plain text into Morse code.
    morse_translation = []
    for character in text.upper():
        if character in MORSE_CODE:  # Only letters and numbers
            morse_translation.append(MORSE_CODE[character])
        else:
            # Ignore characters that are not in Morse dictionary
            continue
    return " ".join(morse_translation)


# Step 2: Input Handling
while True:
    try:
        message = input("\nEnter a message to convert to Morse code: ").strip()

        # Check if input is empty
        if not message:
            print("⚠️ Input cannot be empty. Please enter some text.")
            continue

        # Convert to Morse
        morse_result = text_to_morse(message)

        if not morse_result:
            print("⚠️ No valid letters or numbers found in your input. Try again.")
            continue

        print("\n✅ Morse Code Translation:")
        print(morse_result)
        break  # Exit loop once valid conversion is done

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
