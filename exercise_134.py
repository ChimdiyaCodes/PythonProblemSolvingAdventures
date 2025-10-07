# Exercise 134: Unique Characters

# Create a program that determines and displays the number of unique characters in a
# string entered by the user. For example, Hello, World! has 10 unique characters
# whilezzzhas only one unique character. Use a dictionary or set to solve this problem.

# solution

def count_unique_characters(text):
    """
    This function takes a string (text) and returns the number of unique characters.
    """
    # Convert text into a set (this removes duplicates)
    unique_chars = set(text)

    # Return the count of unique characters
    return len(unique_chars), unique_chars


def main():
    while True:
        try:
            # Ask user for input
            user_input = input(
                "\nEnter a text to get the number of unique characters: ").strip()

            # Validate input: it must not be empty
            if not user_input:
                raise ValueError("Input cannot be empty.")

            # Call our function to count unique characters
            count, characters = count_unique_characters(user_input)

            # Display result
            print(f"\nYour text has {count} unique characters.")
            print(f"These are: {', '.join(sorted(characters))}")

            # End the loop after successful execution
            break

        except ValueError as e:
            # Handle input validation errors
            print(f"Error: {e} Please try again.\n")

        except Exception as e:
            # Catch any unexpected error
            print(f"An unexpected error occurred: {e}")
            break


# This ensures the program runs when executed directly
if __name__ == "__main__":
    main()
