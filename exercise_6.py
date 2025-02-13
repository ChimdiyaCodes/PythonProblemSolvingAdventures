# Exercise 6: Tax and Tip

# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places.

# Solution:

# Prompt the user for the meal cost and tax rate

meal_cost = float(input("How much did your meal cost in dollars? "))
tax_rate = float(input("What is your local tax rate in percentage? "))

# Calculate the tax
tax = meal_cost * (tax_rate / 100)

# Calculate the tip (18% of the meal cost)
tip = meal_cost * 0.18

# Calculate the grand total
grand_total = meal_cost + tax + tip

# Display the results
print(f"\nThe cost of your meal is: ${meal_cost:.2f}")
print(f"\nYour tax is ${tax:.2f}")
print(f"\nYour tip is ${tip:.2f}")
print(f"\nThe grand total cost of your meal is ${grand_total:.2f}")
