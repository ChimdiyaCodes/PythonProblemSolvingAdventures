# Exercise 137: Scrabble™ Score

# In the game of Scrabble™, each letter has points associated with it. The total score
# of a word is the sum of the scores of its letters. More common letters are worth fewer
# points while less common letters are worth more points. The points associated with
# each letter are shown below:
# One point A, E, I, L, N, O, R, S, T and U
# Two points D and G
# Three points B, C, M and P
# Four points F, H, V, W and Y
# Five points K
# Eight points J and X
# Ten points Q and Z
# Write a program that computes and displays the Scrabble™ score for a word.
# Create a dictionary that maps from letters to point values. Then use the dictionary to
# compute the score.
# A Scrabble™ board includes some squares that multiply the value of a letter
# or the value of an entire word. We will ignore these squares in this exercise.

# solution

def get_scrabble_score(word):
    """Returns the Scrabble score of a cleaned word."""

    # Dictionary of Scrabble scores
    scores = {
        "A": 1, "E": 1, "I": 1, "L": 1, "N": 1,
        "O": 1, "R": 1, "S": 1, "T": 1, "U": 1,
        "D": 2, "G": 2,
        "B": 3, "C": 3, "M": 3, "P": 3,
        "F": 4, "H": 4, "V": 4, "W": 4, "Y": 4,
        "K": 5,
        "J": 8, "X": 8,
        "Q": 10, "Z": 10
    }

    # Clean the word: only keep letters (ignore punctuation & spaces)
    cleaned_word = ""
    for char in word:
        if char.isalpha():
            cleaned_word += char.upper()

    # Score calculation
    total = 0
    score_breakdown = []  # To explain scoring later

    for letter in cleaned_word:
        letter_score = scores.get(letter, 0)  # Get value safely
        total += letter_score
        score_breakdown.append(f"{letter}({letter_score})")  # For explanation

    return total, cleaned_word, score_breakdown


# MAIN PROGRAM LOOP
while True:
    word = input("Enter a word (or phrase): ").strip()

    # Input validation – must contain at least 1 letter
    if not any(char.isalpha() for char in word):
        print("❌ Error: Please enter at least one alphabetic character.\n")
        continue

    total_score, cleaned_word, details = get_scrabble_score(word)

    print("\n--- SCRABBLE™ SCORE RESULT ---")
    print(f"Cleaned word: {cleaned_word}")
    print(f"Score breakdown: {' + '.join(details)}")
    print(f"→ TOTAL SCORE: {total_score}\n")

    # Ask to play again
    play_again = input("Do you want to score another word? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing! Goodbye!")
        break
