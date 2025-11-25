# Exercise 144: Number the Lines in a File

# Create a program that adds line numbers to a file. The name of the input file will be
# read from the user, as will the name of the new file that your program will create.
# Each line in the output file should begin with the line number, followed by a colon
# and a space, followed by the line from the input file.

# solution

# Read the input and output file names from the user
input_file = input("Enter the name of the input file: ")
output_file = input("Enter the name of the output file: ")

try:
    # Open the input file for reading
    with open(input_file, 'r') as infile:
        # Open/create the output file for writing
        with open(output_file, 'w') as outfile:
            # Loop through each line in the input file with its line number
            for line_number, line in enumerate(infile, start=1):
                # Write line number followed by the line content
                outfile.write(f"{line_number}: {line}")

    print("Line numbering complete!")

except FileNotFoundError:
    print("Error: The input file was not found.")
