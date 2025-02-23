# Exercise 33: Day Old Bread

# A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
# percent. Write a program that begins by reading the number of loaves of day old
# bread being purchased from the user. Then your program should display the regular
# price for the bread, the discount because it is a day old, and the total price. All of the
# values should be displayed using two decimal places, and the decimal points in all
# of the numbers should be aligned when reasonable values are entered by the user.

# Solution:

# Take input from user
while True:
    try:
        number_of_loaves = int(
            input("\nHow many loaves of day old bread are you buying? "))

        # Validate input
        if number_of_loaves <= 0:
            print("\nNumber of loaves must be a positive value. Please try again.")
        else:
            break  # Exit the loop if input is valid
    except ValueError:
        print("\nInvalid input. Please enter a valid integer.")

# Calculate the regular price
regular_price = number_of_loaves * 3.49

# Calculate discount
discount = regular_price * 0.60

# Calculate total price
total_price = regular_price - discount

# Display results with aligned decimal points
print("\nReceipt:")
print(f"Regular price: ${regular_price:>8.2f}")
print(f"Discount:      ${discount:>8.2f}")
print(f"Total price:   ${total_price:>8.2f}")
