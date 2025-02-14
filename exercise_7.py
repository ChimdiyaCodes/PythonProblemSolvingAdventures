# Exercise 7: Sum of the First n Positive Integers

# Write a program that reads a positive integer, n, from the user and then displays the
# sum of all of the integers from 1 to n. The sum of the first n positive integers can be
# computed using the formula:
# sum = (n * (n + 1)/ 2

# Solution:

# Take input from the user
n = int(input("Enter a positive integer: "))

# Validate input
if n <= 0:
    print("Please enter a positive integer.")
else:
    # Calculate the sum of the first n positive integers
    total_sum = (n * (n + 1)) // 2  # Use integer division

    # Display the result
    print(f"The sum of the first {n} positive integers is: {total_sum}")
