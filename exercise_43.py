# Exercise 43: Faces on Money

# It is common for images of a country’s previous leaders, or other individuals of his￾torical significance, to appear on its money. The individuals that appear on banknotes
# in the United States are listed in Table 2.1.
# Write a program that begins by reading the denomination of a banknote from the
# user. Then your program should display the name of the individual that appears on the banknote of the entered amount.
# Table 2.1 Individuals that
# appear on Banknotes
# Individual Amount
# George Washington $1
# Thomas Jefferson $2
# Abraham Lincoln $5
# Alexander Hamilton $10
# Andrew Jackson $20
# Ulysses S. Grant $50
# Benjamin Franklin $100
# An appropriate error message should be displayed
# if no such note exists.

# solution:

# Define the mapping of banknote denominations to individuals

banknotes = {
    1: "George Washington",
    2: "Thomas Jefferson",
    5: "Abraham Lincoln",
    10:  "Alexander Hamilton",
    20: "Andrew Jackson",
    50: "Ulysses S. Grant",
    100: "Benjamin Franklin"

}

while True:
    try:
        # Prompt the user for input
        # Remove leading/trailing whitespace
        user_input = input(
            "\nEnter the denomination of the banknote: ").strip()
        user_input = user_input.replace('$', '')  # Remove all $ characters
        denomination = int(user_input)  # Convert to integer

        # Check if the denomination exists in the banknotes dictionary
        if denomination in banknotes:
            individual = banknotes[denomination]
            print(f"\n{individual} appears on the ${denomination} banknote.")
            break
        else:
            print("No such note exists. Please, try again!")
            continue

    except ValueError:
        # Handle non-numeric input
        print("Invalid input. Please enter a valid numeric denomination.")
