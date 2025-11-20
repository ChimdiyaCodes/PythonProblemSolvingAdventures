# Exercise 138: Create a Bingo Card

# A Bingo card consists of 5 columns of 5 numbers. The columns are labeled with the
# letters B, I, N, G and O. There are 15 numbers that can appear under each letter. In
# particular, the numbers that can appear under the B range from 1 to 15, the numbers
# that can appear under the I range from 16 to 30, the numbers that can appear under
# the N range from 31 to 45, and so on.
# Write a function that creates a random Bingo card and stores it in a dictionary. The
# keys will be the letters B, I, N, G and O. The values will be the lists of five numbers
# that appear under each letter. Write a second function that displays the Bingo card
# with the columns labeled appropriately. Use these functions to write a program that
#  displays a random Bingo card. Ensure that the main program only runs when the file
# containing your solution has not been imported into another program.
# You may be aware that Bingo cards often have a “free” space in the middle of
# the card. We won’t consider the free space in this exercise.

# solution

import random  # Import random module to generate random numbers


def create_bingo_card():
    """
    Creates a random Bingo card and returns it as a dictionary.
    Keys: 'B', 'I', 'N', 'G', 'O'
    Values: List of random numbers within their specific ranges.
    """
    bingo_card = {
        "B": random.sample(range(1, 16), 5),
        "I": random.sample(range(16, 31), 5),
        "N": random.sample(range(31, 46), 5),
        "G": random.sample(range(46, 61), 5),
        "O": random.sample(range(61, 76), 5),
    }
    return bingo_card


def display_bingo_card(card):
    """
    Displays the Bingo card in a formatted 5x5 table.
    """
    print(" B   I   N   G   O")  # Header

    for row in range(5):  # We need 5 rows
        for letter in "BINGO":  # Go through each column
            print(f"{card[letter][row]:2}", end="  ")  # Print numbers aligned
        print()  # New line after each row


if __name__ == "__main__":  # Only runs when file is executed directly
    card = create_bingo_card()
    display_bingo_card(card)
