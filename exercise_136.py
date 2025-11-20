# Exercise 136: Anagrams Again

# The notion of anagrams can be extended to multiple words. For example, “William
# Shakespeare” and “I am a weakish speller” are anagrams when capitalization and
# spacing are ignored.

# Extend your program from Exercise 135 so that it is able to check if two phrases
# are anagrams.

def clean_phrase(phrase):
    """
    Removes all non-alphabetic characters and converts to lowercase.
    Example: "William Shakespeare!" -> "williamshakespeare"
    """
    cleaned = ""
    for char in phrase:
        if char.isalpha():   # keep only letters
            cleaned += char.lower()
    return cleaned


def are_anagrams(phrase1, phrase2):
    # Clean both phrases first
    phrase1 = clean_phrase(phrase1)
    phrase2 = clean_phrase(phrase2)

    # Compare sorted letters
    return sorted(phrase1) == sorted(phrase2)


while True:
    try:
        phrase1 = input("Enter the first phrase: ").strip()
        phrase2 = input("Enter the second phrase: ").strip()

        # Validation: At least one alphabetic character must exist
        if not any(char.isalpha() for char in phrase1) or not any(char.isalpha() for char in phrase2):
            print(
                "❌ Error: Each phrase must contain at least one alphabetic character.\n")
            continue

        # Check if they are anagrams
        if are_anagrams(phrase1, phrase2):
            print(f"✔️ The phrases are ANAGRAMS! 🎉")
        else:
            print(f"❌ The phrases are NOT anagrams.")

        break  # End program after successful check

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please try again.\n")
