# Exercise 26: Current Time

# Python includes a library of functions for working with time, including a function
# called asctime in the time module. It reads the current time from the computer’s internal clock and returns it in a human-readable format. Write a program
# that displays the current time and date. Your program will not require any input from
# the user.

# import the time module
import time

# Use asctime to get the current time and date in a human-readable format
current_time = time.asctime()

# Display the current time and date
print(f"\nThe current time and date is {current_time}")
