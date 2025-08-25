# Exercise 119: Dealing Hands of Cards

# In many card games each player is dealt a specific number of cards after the deck
# has been shuffled. Write a function, deal, which takes the number of hands, the
# number of cards per hand, and a deck of cards as its three parameters. Your function
# should return a list containing all of the hands that were dealt. Each hand will be
# represented as a list of cards.
# When dealing the hands, your function should modify the deck of cards passed
# to it as a parameter, removing each card from the deck as it is added to a player’s
# hand. When cards are dealt, it is customary to give each player a card before any
# player receives an additional card. Your function should follow this custom when
# constructing the hands for the players.
# Use your solution to Exercise 118 to help you construct a main program that
# creates and shuffles a deck of cards, and then deals out four hands of five cards each.
# Display all of the hands of cards, along with the cards remaining in the deck after
# the hands have been dealt.

import random

# Step 1: Create deck


def createDeck():
    suits = ["♠", "♥", "♦", "♣"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = []
    for suit in suits:
        for value in values:
            deck.append(value + suit)
    return deck

# Step 2: Shuffle the deck (Fisher-Yates method)


def shuffle(deck):
    n = len(deck)
    for i in range(n):
        j = random.randint(i, n - 1)
        deck[i], deck[j] = deck[j], deck[i]

# Step 3: Deal function


def deal(num_hands, cards_per_hand, deck):
    # Validation: enough cards?
    if num_hands * cards_per_hand > len(deck):
        raise ValueError("Not enough cards in the deck to deal.")

    # Create empty hands
    hands = [[] for _ in range(num_hands)]

    # Deal round-robin
    for _ in range(cards_per_hand):
        for hand in hands:
            card = deck.pop(0)   # Take top card
            hand.append(card)

    return hands

# Step 4: Main program


def main():
    deck = createDeck()
    shuffle(deck)

    print("\nDeck has been shuffled.")
    print(f"The deck has {len(deck)} cards.\n")

    while True:
        try:
            num_hands = int(input("\nEnter number of hands (players): "))
            cards_per_hand = int(input("\nEnter number of cards per hand: "))

            # Validation: positive numbers only
            if num_hands <= 0 or cards_per_hand <= 0:
                print("Both values must be positive integers. Try again.\n")
                continue

            total_needed = num_hands * cards_per_hand
            if total_needed > len(deck):
                print(f"Error: You requested {total_needed} cards, "
                      f"but only {len(deck)} are available.\n")
                continue

            hands = deal(num_hands, cards_per_hand, deck)
            break  # If successful, exit loop

        except ValueError as e:
            print(f"Error: {e}. Please try again.\n")
        except Exception:
            print("Invalid input. Please enter valid numbers.\n")

    # Show hands
    for i, hand in enumerate(hands, start=1):
        print(f"\nHand {i}: {hand}")

    # Show remaining cards
    print(f"\nRemaining cards in deck ({len(deck)} left):")
    print(deck)


if __name__ == "__main__":
    main()
