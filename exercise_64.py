# Exercise 64: No More Pennies

# February 4, 2013 was the last day that pennies were distributed by the Royal Canadian
# Mint. Now that pennies have been phased out retailers must adjust totals so that they
# are multiples of 5 cents when they are paid for with cash (credit card and debit card
# transactions continue to be charged to the penny). While retailers have some freedom
# in how they do this, most choose to round to the closest nickel.
# Write a program that reads prices from the user until a blank line is entered.
# Display the total cost of all the entered items on one line, followed by the amount
# due if the customer pays with cash on a second line. The amount due for a cash
# payment should be rounded to the nearest nickel. One way to compute the cash
# payment amount is to begin by determining how many pennies would be needed to
# pay the total. Then compute the remainder when this number of pennies is divided
# by 5. Finally, adjust the total down if the remainder is less than 2.5. Otherwise adjust
# the total up.

# solution:

def round_to_nearest_nickel(total):
    """
    Rounds the total to the nearest nickel (5 cents).
    """
    # Convert total to pennies
    total_in_pennies = int(round(total * 100))

    # Calculate remainder when divided by 5
    remainder = total_in_pennies % 5

    # Adjust total to the nearest nickel
    if remainder < 2.5:
        total_in_pennies -= remainder
    else:
        total_in_pennies += (5 - remainder)

    # Convert back to dollars
    return total_in_pennies / 100


def main():
    total_cost = 0.0

    print("Enter prices of items (one per line). Press Enter on a blank line to finish.")

    while True:
        price_input = input("Enter the price of the item: ").strip()

        # Exit loop if the input is a blank line
        if price_input == "":
            break

        try:
            # Convert input to a float
            price = float(price_input)

            # Ensure the price is non-negative
            if price < 0:
                print("Price cannot be negative. Please enter a valid price.")
                continue

            # Add the price to the total cost
            total_cost += price

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Display the total cost
    print(f"\nTotal cost of all items: ${total_cost:.2f}")

    # Calculate and display the cash payment amount
    cash_payment = round_to_nearest_nickel(total_cost)
    print(f"Amount due if paying with cash: ${cash_payment:.2f}")


if __name__ == "__main__":
    main()
