# Exercise 140: Play Bingo

# In this exercise you will write a program that simulates a game of Bingo for a single
# card. Begin by generating a list of all of the valid Bingo calls (B1 through O75). Once
# the list has been created you can randomize the order of its elements by calling the
# shufflefunction in therandommodule. Then your program should consume calls
# out of the list, crossing out numbers on the card, until the card contains a crossed out
# line (horizontal, vertical or diagonal). Simulate 1,000 games and report the minimum,
# maximum and average number of calls that must be made before the card wins. Import
# your solutions to Exercises 138 and 139 when completing this exercise.

import random
import sys
import traceback

# Try to import the functions from your files named exactly as you said:
# exercise_138.py and exercise_139.py
try:
    from exercise_138 import create_bingo_card
except Exception as e:
    print("Warning: could not import create_bingo_card from exercise_138.py.")
    print("Import error:", e)
    print("Traceback (most recent call last):")
    traceback.print_exc(limit=1)
    create_bingo_card = None

try:
    from exercise_139 import is_winning_card
except Exception as e:
    print("Warning: could not import is_winning_card from exercise_139.py.")
    print("Import error:", e)
    print("Traceback (most recent call last):")
    traceback.print_exc(limit=1)
    is_winning_card = None

# --- Fallback implementations (used only if imports failed) ---
# These are simple copies of the needed functionality so the simulation runs.
if create_bingo_card is None:
    def create_bingo_card():
        """Fallback: create a bingo card (dict of lists)"""
        return {
            "B": random.sample(range(1, 16), 5),
            "I": random.sample(range(16, 31), 5),
            "N": random.sample(range(31, 46), 5),
            "G": random.sample(range(46, 61), 5),
            "O": random.sample(range(61, 76), 5),
        }

if is_winning_card is None:
    def is_winning_card(card):
        """Fallback: check horizontal, vertical, diagonal lines of zeros"""
        grid = [[card[col][row] for col in "BINGO"] for row in range(5)]

        # horizontal
        for row in grid:
            if sum(row) == 0:
                return True

        # vertical
        for col in range(5):
            if sum(grid[row][col] for row in range(5)) == 0:
                return True

        # main diagonal
        if sum(grid[i][i] for i in range(5)) == 0:
            return True

        # anti-diagonal
        if sum(grid[i][4 - i] for i in range(5)) == 0:
            return True

        return False

# --------------------------------------------------------------
# Helper utilities for Exercise 140
# --------------------------------------------------------------


def generate_bingo_calls():
    """Return list of strings 'B1'..'B15', 'I16'..'I30', ..., 'O75'."""
    calls = []
    calls += [f"B{n}" for n in range(1, 16)]
    calls += [f"I{n}" for n in range(16, 31)]
    calls += [f"N{n}" for n in range(31, 46)]
    calls += [f"G{n}" for n in range(46, 61)]
    calls += [f"O{n}" for n in range(61, 76)]
    return calls


def cross_out_number(card, call):
    """
    Given a call like 'B12', mark that number as called on the card by replacing
    it with 0 if it exists in the specified column.
    """
    col = call[0]  # letter e.g. 'B'
    try:
        num = int(call[1:])  # the numeric part e.g. 12
    except ValueError:
        return  # malformed call -- ignore

    # Look for the number in the column and replace with 0
    for i in range(5):
        if card[col][i] == num:
            card[col][i] = 0
            break


def simulate_one_game():
    """
    Create a fresh card, shuffle the 75 calls, call numbers until the card wins.
    Return the number of calls needed.
    """
    card = create_bingo_card()
    calls = generate_bingo_calls()
    random.shuffle(calls)

    for i, call in enumerate(calls, start=1):
        cross_out_number(card, call)
        if is_winning_card(card):
            return i  # calls used until win

    return 75  # fallback, should never really happen because a card must win by 75 calls


def simulate_games(n_games=1000):
    results = []
    for _ in range(n_games):
        results.append(simulate_one_game())
    return results


def print_stats(results):
    minimum = min(results)
    maximum = max(results)
    average = sum(results) / len(results)
    print("\n=== Simulation Results ===")
    print(f"Games simulated: {len(results)}")
    print(f"Minimum calls until win: {minimum}")
    print(f"Maximum calls until win: {maximum}")
    print(f"Average calls until win: {average:.2f}")


def main():
    N = 1000
    print(f"Simulating {N} Bingo games for one card each...")
    results = simulate_games(N)
    print_stats(results)


if __name__ == "__main__":
    main()
