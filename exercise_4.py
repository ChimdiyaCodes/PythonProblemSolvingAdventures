# Exercise 4: Area of a field

# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
# Hint: There are 43,560 square feet in an acre.

# Solution:

# Get inputs from user
length = int(input("Enter the length of the field in feet: "))
width = int(input("\nEnter the width of the field in feet: "))

# Calculate area in square feet
area_sq_ft = length * width

# Convert to acres (1 acre = 43,560 square feet)
area_acres = area_sq_ft / 43560

# Display the result in acres, rounded to 2 decimal places
print(f"\nThe area of the field in acres is {area_acres:.2f} acres")
