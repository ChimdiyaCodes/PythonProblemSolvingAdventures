# Exercise 62: Discount Table

# A particular retailer is having a 60 percent off sale on a variety of discontinued
# products. The retailer would like to help its customers determine the reduced price
# of the merchandise by having a printed discount table on the shelf that shows the
# original prices and the prices after the discount has been applied. Write a program that
# uses a loop to generate this table, showing the original price, the discount amount,
# and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure
# that the discount amounts and the new prices are rounded to 2 decimal places when
# they are displayed.

# solution

def generate_discount_table():
    # List of original prices
    original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]

    # Discount rate (60%)
    discount_rate = 0.60

    # Print the table header
    print(f"{'Original Price':<16} {'Discount Amount':<16} {'New Price':<16}")
    print("-" * 45)

    # Loop through each original price and calculate the discount and new price
    for price in original_prices:
        discount_amount = price * discount_rate
        new_price = price - discount_amount

        # Format the discount amount and new price using :.2f
        discount_amount_formatted = f"{discount_amount:.2f}"
        new_price_formatted = f"{new_price:.2f}"

        # Print the formatted row
        print(
            f"${price:<14} ${discount_amount_formatted:<14} ${new_price_formatted:<14}")


# Generate the discount table
generate_discount_table()
