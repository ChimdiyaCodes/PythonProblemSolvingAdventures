# Exercise 80: Coin Flip Simulation

# What’s the minimum number of times you have to flip a coin before you can have
# three consecutive flips that result in the same outcome (either all three are heads or
# all three are tails)? What’s the maximum number of flips that might be needed? How many flips are needed on average? In this exercise we will explore these questions
# by creating a program that simulates several series of coin flips.
# Create a program that uses Python’s random number generator to simulate flipping
# a coin several times. The simulated coin should be fair, meaning that the probability
# of heads is equal to the probability of tails. Your program should flip simulated
# coins until either 3 consecutive heads of 3 consecutive tails occur. Display an H each
# time the outcome is heads, and a T each time the outcome is tails, with all of the
# outcomes shown on the same line. Then display the number of flips needed to reach
# 3 consecutive flips with the same outcome. When your program is run it should
# perform the simulation 10 times and report the average number of flips needed.
# Sample output is shown below:
# HTTT (4 flips)
# THHH (4 flips)
# HHTTHTHTTHHTHTT HTTT (19 flips)
# TTT (3 flips)
# THTTHTHHTTHHTHTΗΗΗ (18 flips)
# TTHTTHTHTHHH (12 flips)
# HHH (3 flips)
# HTTHHH (6 flips)
# THTTT (5 flips)
# THTTT (5 flips).
# On average, 7.9 flips were needed.

# solution:

import random


def coin_flip_simulation():
    sequence = []
    count = 0
    while True:
        outcome = random.choice(['H', 'T'])
        sequence.append(outcome)
        count += 1
        if count >= 3:
            if sequence[-1] == sequence[-2] == sequence[-3]:
                return ''.join(sequence), count


def main():
    total_flips = 0
    num_simulations = 10
    for i in range(num_simulations):
        sequence, flips = coin_flip_simulation()
        print(f"{sequence} ({flips} flips)")
        total_flips += flips
    average = total_flips / num_simulations
    print(f"On average, {average:.1f} flips were needed.")


if __name__ == "__main__":
    main()
