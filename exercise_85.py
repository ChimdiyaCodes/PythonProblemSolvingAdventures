# Exercise 85: Convert an Integer to its Ordinal Number

# Words like first, second and third are referred to as ordinal numbers. In this exercise,
# you will write a function that takes an integer as its only parameter and returns a
# string containing the appropriate English ordinal number as its only result. Your
# function must handle the integers between 1 and 12 (inclusive). It should return an
# empty string if a value outside of this range is provided as a parameter. Include a
# main program that demonstrates your function by displaying each integer from 1 to
# 12 and its ordinal number. Your main program should only run when your file has
# not been imported into another program.

# solution

def convert_to_ordinal(n):
    """
    Converts an integer from 1 to 12 into its ordinal string.
    Returns an empty string if the input is outside this range.
    """
    ordinals = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth"
    }

    return ordinals.get(n, "")  # Returns "" if n not in dictionary


def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("\nOrdinal numbers from 1 to 12:")
    for i in range(1, 13):
        print(f"{i} → {convert_to_ordinal(i)}")

    # Optional: Ask user to test their own input
    while True:
        user_choice = input(
            "\nDo you want to test a custom number? (yes/no): ").strip().lower()
        if user_choice == "yes":
            user_num = get_valid_integer("Enter a number between 1 and 12: ")
            result = convert_to_ordinal(user_num)
            if result:
                print(f"\n{user_num} → {result}")
            else:
                print(
                    "Number out of supported range. Please enter a number between 1 and 12.")
        elif user_choice == "no":
            print("\nGoodbye!")
            break
        else:
            print("Please type 'yes' or 'no'.")


# This ensures main() only runs if this script is executed directly
if __name__ == "__main__":
    main()
