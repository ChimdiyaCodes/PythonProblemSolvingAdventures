# Exercise 129: Two Dice Simulation

# In this exercise you will simulate 1,000 rolls of two dice. Begin by writing a function that simulates rolling a pair of six-sided dice. Your function will not take any
# parameters. It will return the total that was rolled on two dice as its only result.
# Write a main program that uses your function to simulate rolling two six-sided
# dice 1,000 times. As your program runs, it should count the number of times that each
# total occurs. Then it should display a table that summarizes this data. Express the
# frequency for each total as a percentage of the total number of rolls. Your program
# should also display the percentage expected by probability theory for each total.

# solution

import random


def roll_two_dice():
    """Simulates rolling two six-sided dice and returns their sum."""
    die1 = random.randint(1, 6)  # roll first die
    die2 = random.randint(1, 6)  # roll second die
    return die1 + die2


def main():
    rolls = 1000
    counts = {total: 0 for total in range(2, 13)}  # dictionary for counts

    # Simulate 1000 rolls
    for n in range(rolls):
        total = roll_two_dice()
        counts[total] += 1

    # Theoretical probabilities (ways to make each total)
    ways = {
        2: 1, 3: 2, 4: 3, 5: 4, 6: 5,
        7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1
    }

    print(f"{'Total':<6}{'Simulated %':<15}{'Theoretical %':<15}")
    for total in range(2, 13):
        simulated_percentage = (counts[total] / rolls) * 100
        theoretical_percentage = (ways[total] / 36) * 100
        print(f"{total:<6}{simulated_percentage:<15.2f}{theoretical_percentage:<15.2f}")


if __name__ == "__main__":
    main()
