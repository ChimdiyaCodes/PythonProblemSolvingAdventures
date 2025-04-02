# Exercise 83: Shipping Calculator

# An online retailer provides express shipping for many of its items at a rate of $10.95
# for the first item, and $2.95 for each subsequent item. Write a function that takes the
# number of items in the order as its only parameter. Return the shipping charge for
# the order as the function’s result. Include a main program that reads the number of
# items purchased from the user and displays the shipping charge.

# solution:

# Constants for shipping rates (easy to update)
FIRST_ITEM_COST = 10.95  # Shipping cost for the first item
ADDITIONAL_ITEM_COST = 2.95  # Shipping cost for each additional item


def calculate_shipping_cost(num_items):
    """
    Calculates the shipping cost based on the number of items.

    Parameters:
        num_items (int): Number of items in the order.

    Returns:
        float: Total shipping cost in dollars.
    """
    if num_items < 1:
        return 0.00  # Edge case (should not happen due to input validation)
    elif num_items == 1:
        return FIRST_ITEM_COST
    else:
        return FIRST_ITEM_COST + (num_items - 1) * ADDITIONAL_ITEM_COST


def get_valid_item_count():
    """
    Continuously prompts the user until a valid positive integer is entered.

    Returns:
        int: Valid number of items.
    """
    while True:
        try:
            num_items = int(input("Enter the number of items purchased: "))
            if num_items < 1:
                print("Error: Number of items must be at least 1.")
            else:
                return num_items
        except ValueError:
            print("Error: Please enter a whole number (e.g., 1, 2, 3).")


def main():
    print("Shipping Cost Calculator")
    print("------------------------")

    # Get valid input
    num_items = get_valid_item_count()

    # Calculate shipping cost
    shipping_cost = calculate_shipping_cost(num_items)

    # Display result
    print(f"\nShipping cost for {num_items} item(s): ${shipping_cost:.2f}")


if __name__ == "__main__":
    main()
