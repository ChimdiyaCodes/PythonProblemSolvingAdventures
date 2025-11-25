# Exercise 141: Display the Head of a File

# Unix-based operating systems usually include a tool named head. It displays the
# first 10 lines of a file whose name is provided as a command line parameter. Write
# a Python program that provides the same behavior. Display an appropriate error
# message if the file requested by the user does not exist or if the command line
# parameter is omitted.

# solution

import sys

# STEP 1: Check if filename was provided
if len(sys.argv) < 2:
    print("Error: Missing command line argument. Please provide a filename.")
    sys.exit()  # Stop the program here

filename = sys.argv[1]  # Get the filename from the command line

# STEP 2: Try to open the file
try:
    with open(filename, 'r') as file:  # Open file in read mode
        # STEP 3: Read and display first 10 lines
        for i in range(10):
            line = file.readline()  # Read one line at a time
            if not line:  # Stop if file has fewer than 10 lines
                break
            print(line, end="")  # Print without adding extra new line

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
