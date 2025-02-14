# Exercise 9: Compound Interest

# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.

# Solution:

# Define constants
INTEREST_RATE = 0.04  # 4% annual interest
MAX_YEARS = 3

while True:
    try:
        # Get initial deposit from user
        principal = float(input("\nEnter the initial deposit amount: $"))

        # Validate the input
        if principal < 0:
            print("Error: Please enter a non-negative deposit amount.")
            continue

        # Calculate and display balance for each year
        for year in range(1, MAX_YEARS + 1):
            balance = principal * (1 + INTEREST_RATE) ** year
            balance_rounded = round(balance, 2)
            print(
                f"\nYour account balance after {year} year(s): ${balance_rounded:,.2f}")

        # Ask if user wants to calculate another deposit
        retry = input(
            "\nWould you like to calculate another deposit? (yes/no): ").lower()
        if retry != 'Yes':
            print("\nThank you for using the compound interest calculator!")
            break

    except ValueError:
        print("Error: Please enter a valid number.")
        continue
