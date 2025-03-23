# Exercise 70: Caesar Cipher

# One of the first known examples of encryption was used by Julius Caesar. Caesar
# needed to provide written instructions to his generals, but he didn’t want his enemies
# This copy belongs to 'acha04'
# Exercise 70: Caesar Cipher 33
# to learn his plans if the message slipped into their hands. As result, he developed
# what later became known as the Caesar Cipher.
# The idea behind this cipher is simple (and as a result, it provides no protection
# against modern code breaking techniques). Each letter in the original message is
# shifted by 3 places. As a result, A becomes D, B becomes E, C becomes F, D
# becomes G, etc. The last three letters in the alphabet are wrapped around to the
# beginning: X becomes A, Y becomes B and Z becomes C. Non-letter characters are
# not modified by the cipher.
# Write a program that implements a Caesar cipher. Allow the user to supply the
# message and the shift amount, and then display the shifted message. Ensure that
# your program encodes both uppercase and lowercase letters. Your program should
# also support negative shift values so that it can be used both to encode messages and
# decode messages.

# solution:

def caesar_cipher(message, shift):
    """
    Applies the Caesar cipher to the given message with the specified shift.

    Args:
        message (str): The message to encrypt/decrypt
        shift (int): The number of positions to shift each letter
                     (positive for encryption, negative for decryption)

    Returns:
        str: The encrypted/decrypted message
    """
    result = ""

    for char in message:
        if char.isalpha():
            # Determine the ASCII offset based on case
            ascii_offset = ord('A') if char.isupper() else ord('a')

            # Convert to 0-25 range, apply shift, and handle wrapping
            # Using modulo 26 ensures we wrap around the alphabet
            shifted_position = (ord(char) - ascii_offset + shift) % 26

            # Convert back to ASCII and then to character
            result += chr(shifted_position + ascii_offset)
        else:
            # Non-letter characters remain unchanged
            result += char

    return result


def main():
    """Main function to run the Caesar cipher program."""
    print("\nWelcome To The Caesar Cipher Program For Message Encryption!")
    print("========================================================")

    while True:
        try:
            # Get message input
            message = input("\nEnter the message to encrypt/decrypt: ")

            # Validate message isn't empty
            if not message:
                print("Error: Message cannot be empty. Please try again.")
                continue

            # Get shift amount
            shift_input = input(
                "Enter the shift amount (positive to encrypt, negative to decrypt): ")
            shift = int(shift_input)

            # Apply the cipher
            result = caesar_cipher(message, shift)

            # Display the result
            print("\nResult:")
            print(result)

            # Ask if the user wants to continue
            another = input(
                "\nDo you want to encrypt/decrypt another message? (y/n): ").lower()
            if another != 'y':
                print("Thank you for using the Caesar Cipher program!")
                break

        except ValueError:
            print("Error: Shift amount must be an integer. Please try again.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
