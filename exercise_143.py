# Exercise 143: Concatenate Multiple Files

# Unix-based operating systems typically include a tool named cat, which is short
# for concatenate. Its purpose is to concatenate and display one or more files whose
# names are provided as command line parameters. The files are displayed in the same
# order that they appear on the command line.
# Create a Python program that performs this task. It should generate an appropriate
# error message for any file that cannot be displayed, and then proceed to the next file.
# Display an appropriate error message if your program is started without any command
# line parameters.

# solution

import sys

# STEP 1: Check if any filenames were provided
if len(sys.argv) < 2:
    print("Error: No files provided. Please enter at least one filename.")
    sys.exit()

# STEP 2: Loop through each file provided
for filename in sys.argv[1:]:  # Skip index 0 (program name)
    try:
        # STEP 3: Open and display file contents
        with open(filename, 'r') as file:
            # Optional: To label files
            print(f"\n--- Contents of {filename} ---")
            for line in file:
                print(line, end="")  # Print file content
    except FileNotFoundError:
        print(
            f"Error: The file '{filename}' does not exist or cannot be opened.")
