# Exercise 167: Recursive Palindrome

# The notion of a palindrome was introduced previously in Exercise 72. In this exer￾cise you will write a recursive function that determines whether or not a string is
# a palindrome. The empty string is a palindrome, as is any string containing only  one character. Any longer string is a palindrome if its first and last characters
# match, and if the string formed by removing the first and last characters is also
# a palindrome.
# Write a main program that reads a string from the user. Use your recursive function
# to determine whether or not the string is a palindrome. Then display an appropriate
# message for the user.

# solution

def is_palindrome_recursive(s):
    """
    Recursively checks if a string is a palindrome.
    Base cases:
        - Empty string
        - Single character
    Recursive step:
        - Compare first and last, then check substring s[1:-1]
    """
    # Base cases
    if len(s) <= 1:
        return True

    # If first and last don't match → not a palindrome
    if s[0] != s[-1]:
        return False

    # Recursive call on the middle substring
    return is_palindrome_recursive(s[1:-1])


def main():
    """
    Reads input, validates, and checks palindrome status using the recursive function.
    """
    while True:
        try:
            text = input(
                "\nEnter a string to check if it's a palindrome: ").strip()

            # Validate empty input
            if not text:
                print("Error: Input cannot be empty. Please try again.")
                continue

            # Optionally normalize input (optional): remove spaces, ignore case
            cleaned_text = text.replace(" ", "").lower()

            # Call recursive function
            if is_palindrome_recursive(cleaned_text):
                print(f"\n✔ '{text}' is a palindrome.")
            else:
                print(f"\n✘ '{text}' is NOT a palindrome.")

            break  # Exit loop once valid input processed

        except Exception as e:
            print(f"Unexpected error: {e}. Try again.")


if __name__ == "__main__":
    main()
