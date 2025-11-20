# Exercise 139: Checking for a Winning Card

# A winning Bingo card contains a line of 5 numbers that have all been called. Players
# normally mark the numbers that have been called by crossing them out or marking
# them with a Bingo dauber. In our implementation we will mark that a number has
# been called by replacing it with a 0 in the Bingo card dictionary.
# Write a function that takes a dictionary representing a Bingo card as its only
# parameter. If the card contains a line of five zeros (vertical, horizontal or diagonal)
# then your function should return True, indicating that the card has won. Otherwise
# the function should return False.
# Create a main program that demonstrates your function by creating several Bingo
# cards, displaying them, and indicating whether or not they contain a winning line.
# You should demonstrate your function with at least one card with a horizontal line,
# at least one card with a vertical line, at least one card with a diagonal line, and at
# least one card that has some numbers crossed out but does not contain a winning line.
# You will probably want to import your solution to Exercise 138 when completing
# this exercise.
# Hint: Because there are no negative numbers on a Bingo card, finding a line
# of 5 zeros is the same problem as finding a line of 5 entries that sum to zero.
# You may find the summation problem easier to solve.

# solution:

import random

# -----------------------------------------
# Exercise 138 Functions (Already Completed)
# -----------------------------------------


def create_bingo_card():
    """
    Creates a random Bingo card and returns it as a dictionary.
    Keys: 'B', 'I', 'N', 'G', 'O'
    Values: List of random numbers within their valid ranges.
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
    print("\n B   I   N   G   O")
    for row in range(5):
        for col in "BINGO":
            print(f"{card[col][row]:2}", end="  ")
        print()
    print()


# -----------------------------------------
# Exercise 139: Check for a Winning Card
# -----------------------------------------

def is_winning_card(card):
    """
    Checks if the Bingo card contains:
      - A horizontal line of 5 zeros
      - A vertical line of 5 zeros
      - A diagonal line of 5 zeros

    Returns True if any winning line is found, otherwise False.
    """

    # Convert the dict into a 5x5 grid (rows)
    grid = [[card[col][row] for col in "BINGO"] for row in range(5)]

    # Check horizontal lines
    for row in grid:
        if sum(row) == 0:
            return True

    # Check vertical lines
    for col in range(5):
        if sum(grid[row][col] for row in range(5)) == 0:
            return True

    # Check main diagonal (top-left to bottom-right)
    if sum(grid[i][i] for i in range(5)) == 0:
        return True

    # Check anti-diagonal (top-right to bottom-left)
    if sum(grid[i][4 - i] for i in range(5)) == 0:
        return True

    return False


# -----------------------------------------
# Helper functions to modify cards for demo
# -----------------------------------------

def mark_horizontal(card):
    """Force a horizontal winning line on row 2."""
    for col in "BINGO":
        card[col][2] = 0


def mark_vertical(card):
    """Force a vertical winning line on column 'G'."""
    for i in range(5):
        card["G"][i] = 0


def mark_diagonal(card):
    """Force a diagonal winning line."""
    for i, col in enumerate("BINGO"):
        card[col][i] = 0


def mark_non_winning(card):
    """Mark random zeros without forming any winning line."""
    card["B"][0] = 0
    card["I"][3] = 0
    card["N"][1] = 0
    card["G"][4] = 0
    card["O"][2] = 0


# -----------------------------------------
# Main Program
# -----------------------------------------

def main():
    print("\n=== BINGO WINNING CARD CHECK ===")

    # 1. Horizontal winning card
    card1 = create_bingo_card()
    mark_horizontal(card1)
    print("\n--- Horizontal Winning Card ---")
    display_bingo_card(card1)
    print("Winning?", is_winning_card(card1))

    # 2. Vertical winning card
    card2 = create_bingo_card()
    mark_vertical(card2)
    print("\n--- Vertical Winning Card ---")
    display_bingo_card(card2)
    print("Winning?", is_winning_card(card2))

    # 3. Diagonal winning card
    card3 = create_bingo_card()
    mark_diagonal(card3)
    print("\n--- Diagonal Winning Card ---")
    display_bingo_card(card3)
    print("Winning?", is_winning_card(card3))

    # 4. Non-winning card
    card4 = create_bingo_card()
    mark_non_winning(card4)
    print("\n--- Non-Winning Card ---")
    display_bingo_card(card4)
    print("Winning?", is_winning_card(card4))

    print("\n=== END OF DEMO ===\n")


if __name__ == "__main__":
    main()
