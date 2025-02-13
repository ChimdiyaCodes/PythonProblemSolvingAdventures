# Exercise 5: Bottle Deposits

# In many jurisdictions a small deposit is added to drink containers to encourage people
# to recycle them. In one particular jurisdiction, drink containers holding one liter or
# less have a $0.10 deposit, and drink containers holding more than one liter have a
# $0.25 deposit.
# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and always displays exactly two decimal places.

# Solution:

# Ask the user the size and number of containers they have
small_container = int(
    input("How many small containers of less than 1L do you have? "))
large_container = int(
    input("\nHow many large containers of greater than 1L do you have? "))

# Display the number of containers
print(f"\nYou have {small_container} small containers")
print(f"\nYou have {large_container} large containers")

# Calculating the refund
refund_small = small_container * 0.10
refund_large = large_container * 0.25

# Displaying the refund
print(
    f"\nYou are getting a refund of ${refund_small:.2f} for your {small_container} small containers")
print(
    f"and a refund of ${refund_large:.2f} for your {large_container} large containers")

total_refund = refund_small + refund_large
print(f"\nYour total refund is ${total_refund:.2f}")
