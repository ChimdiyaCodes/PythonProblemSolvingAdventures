# Exercise 135: Anagrams

# Two words are anagrams if they contain all of the same letters, but in a different
# order. For example, “evil” and “live” are anagrams because each contains one e, one
# i, one l, and one v. Create a program that reads two strings from the user, determines
# whether or not they are anagrams, and reports the result.

# solution

def are_anagrams(word1, word2):
    # Remove spaces and convert to lowercase
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()

    # Check if sorted letters are the same
    return sorted(word1) == sorted(word2)


while True:
    print("\nThis program asks you for two words and checks if they are Anagrams.")
    try:
        word1 = input("\nEnter the first word: ").strip()
        word2 = input("\nEnter the second word: ").strip()

        # Input validation
        if not word1 or not word2:
            print("❌ Error: You must enter two non-empty words.\n")
            continue

        if not word1.replace(" ", "").isalpha() or not word2.replace(" ", "").isalpha():
            print("❌ Error: Only alphabetic characters are allowed.\n")
            continue

        # Check if they are anagrams
        if are_anagrams(word1, word2):
            print(f"✔️ '{word1}' and '{word2}' are ANAGRAMS! 🎉")
        else:
            print(f"❌ '{word1}' and '{word2}' are NOT anagrams.")

        break

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Please try again.\n")
