# Exercise 60: Roulette Payouts

# A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two
# are green. The green spaces are numbered 0 and 00. The red spaces are numbered 1,
# 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36. The remaining integers
# between 1 and 36 are used to number the black spaces.
# Many different bets can be placed in roulette. We will only consider the following
# subset of them in this exercise:
# • Single number (1 to 36, 0, or 00)
# • Red versus Black
# • Odd versus Even (Note that 0 and 00 do not pay out for even)
# • 1 to 18 versus 19 to 36
# Write a program that simulates a spin of a roulette wheel by using Python’s random
# number generator. Display the number that was selected and all of the bets that must
# be payed. For example, if 13 is selected then your program should display:
# The spin resulted in 13...
# Pay 13
# Pay Black
# Pay Odd
# Pay 1 to 18
# If the simulation results in 0 or 00 then your program should display Pay 0 or
# Pay 00 without any further output.

# solution

import random


def simulate_roulette_spin():
    # Simulate a roulette spin
    result = random.randint(0, 37)  # 37 represents 00
    return result


def determine_payouts(result):
    # Define red and black numbers
    red_numbers = {1, 3, 5, 7, 9, 12, 14, 16,
                   18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
    black_numbers = set(range(1, 37)) - red_numbers

    # Display the result
    if result == 37:
        print("The spin resulted in 00...")
        print("Pay 00")
        return  # No further payouts for 0 or 00
    elif result == 0:
        print("The spin resulted in 0...")
        print("Pay 0")
        return  # No further payouts for 0 or 00
    else:
        print(f"The spin resulted in {result}...")
        print(f"Pay {result}")

    # Determine additional payouts
    if result in red_numbers:
        print("Pay Red")
    elif result in black_numbers:
        print("Pay Black")

    if result != 0 and result != 37:  # 0 and 00 are neither odd nor even
        if result % 2 == 1:
            print("Pay Odd")
        else:
            print("Pay Even")

    if 1 <= result <= 18:
        print("Pay 1 to 18")
    elif 19 <= result <= 36:
        print("Pay 19 to 36")


def main():
    while True:
        try:
            # Prompt the user to spin the wheel
            input("Press Enter to spin the roulette wheel...")
            result = simulate_roulette_spin()
            determine_payouts(result)
            break  # Exit the loop after a valid spin
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


if __name__ == "__main__":
    main()
