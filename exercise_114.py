# Exercise 114: Random Lottery Numbers

# In order to win the top prize in a particular lottery, one must match all 6 numbers
# on his or her ticket to the 6 numbers between 1 and 49 that are drawn by the lottery
# organizer. Write a program that generates a random selection of 6 numbers for a
# lottery ticket. Ensure that the 6 numbers selected do not contain any duplicates.
# Display the numbers in ascending order.

# solution:

import random


def generate_lottery_numbers():
    #  Generates and returns 6 unique random numbers between 1 and 49, sorted in ascending order.
    numbers = random.sample(range(1, 50), 6)
    numbers.sort()
    return numbers


def main():
    print("\n🎟️ Welcome to the Lottery Number Generator!")

    while True:
        ticket = generate_lottery_numbers()
        print(f"\nYour lottery numbers are: {ticket}")

        # Input validation loop
        while True:
            choice = input(
                """\nWould you like to generate another ticket? : 
Enter:
Y for YES
N for NO
→ """
            ).strip().upper()

            if choice in ['Y', 'YES', 'N', 'NO']:
                break
            print("Invalid input! Please enter Y or N.")

        if choice in ['N', 'NO']:
            print("\n🎉 Thank you for using the Lottery Number Generator! Good luck! 🍀")
            break


if __name__ == "__main__":
    main()
