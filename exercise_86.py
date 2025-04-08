# Exercise 86: The Twelve Days of Christmas

# The Twelve Days of Christmas is a repetitive song that describes an increasingly
# long list of gifts sent to one’s true love on each of 12 days. A single gift is sent on
# the first day. A new gift is added to the collection on each additional day, and then
# the complete collection is sent. The first three verses of the song are shown below.
# The complete lyrics are available on the internet.
# On the first day of Christmas
# my true love sent to me:
# A partridge in a pear tree.
# On the second day of Christmas
# my true love sent to me:
# Two turtle doves,
# And a partridge in a pear tree.
# On the third day of Christmas
# my true love sent to me:
# Three French hens,
# Two turtle doves,
# And a partridge in a pear tree.
# Your task is to write a program that displays the complete lyrics for The Twelve
# Days of Christmas. Write a function that takes the verse number as its only parameter
# and displays the specified verse of the song. Then call that function 12 times with
# integers that increase from 1 to 12.
# Each item that is sent to the recipient in the song should only appear once in your
# program, with the possible exception of the partridge. It may appear twice if that
# helps you handle the difference between “A partridge in a pear tree” in the first verse
# and “And a partridge in a pear tree” in the subsequent verses. Import your solution
# to Exercise 85 to help you complete this exercise.

# solution:

def convert_to_ordinal(n):
    """
    Converts a number from 1 to 12 into its ordinal string form.
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
    return ordinals.get(n, "")


def print_verse(day):
    """
    Prints the verse for the given day of The Twelve Days of Christmas.
    """
    gifts = [
        "A partridge in a pear tree.",
        "Two turtle doves,",
        "Three French hens,",
        "Four calling birds,",
        "Five golden rings,",
        "Six geese a-laying,",
        "Seven swans a-swimming,",
        "Eight maids a-milking,",
        "Nine ladies dancing,",
        "Ten lords a-leaping,",
        "Eleven pipers piping,",
        "Twelve drummers drumming,"
    ]

    ordinal = convert_to_ordinal(day)
    print(f"On the {ordinal} day of Christmas")
    print("my true love sent to me:")

    # Reverse loop through the gift list up to the current day
    for i in range(day - 1, -1, -1):
        if i == 0 and day != 1:
            print(f"And {gifts[i]}")
        else:
            print(gifts[i])


def get_valid_day():
    """
    Prompts the user to enter a valid day number (1–12).
    """
    while True:
        try:
            day = int(input("\nEnter a day number (1 to 12): "))
            if 1 <= day <= 12:
                return day
            else:
                print("Please enter a number between 1 and 12.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print("\n🎄 The Twelve Days of Christmas 🎄\n")
    for day in range(1, 13):
        print_verse(day)
        print()  # Blank line between verses

    # Optional: Test custom day
    while True:
        choice = input(
            "\nWould you like to see a specific verse? (yes/no): ").strip().lower()
        if choice == "yes":
            selected_day = get_valid_day()
            print()
            print_verse(selected_day)
            print()
        elif choice == "no":
            print("Goodbye! 🎅")
            break
        else:
            print("Please type 'yes' or 'no'.")


if __name__ == "__main__":
    main()
