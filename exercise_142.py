# Exercise 142: Display the Tail of a File

# Unix-based operating systems also typically include a tool named tail. It displays
# the last 10 lines of a file whose name is provided as a command line parameter.
# Write a Python program that provides the same behavior. Display an appropriate
# error message if the file requested by the user does not exist or if the command line
# parameter is omitted.
# There are several different approaches that can be taken to solve this problem.
# One option is to load the entire contents of the file into a list and then display the
# last 10 elements. Another option is to read the contents of the file twice, once to
# count the lines, and a second time to display the last 10 lines. However, both of these
# solutions are undesirable when working with large files. Another solution exists that
# only requires you to read the file once, and only requires you to store 10 lines from
# the file at one time. For an added challenge, develop such a solution.

# solution

import sys
from collections import deque  # Efficient structure for handling last 10 lines

# STEP 1: Check if filename was provided
if len(sys.argv) < 2:
    print("Error: Missing command line argument. Please provide a filename.")
    sys.exit()

filename = sys.argv[1]

# STEP 2: Try to open and read efficiently
try:
    with open(filename, 'r') as file:
        last_lines = deque(file, maxlen=10)  # Keep only last 10 lines

        # Print the stored lines
        for line in last_lines:
            print(line, end="")

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
