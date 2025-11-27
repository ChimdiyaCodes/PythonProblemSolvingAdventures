# Exercise 150: Remove Comments

# Python uses the # character to mark the beginning of a comment. The comment ends
# at the end of the line containing the # character. In this exercise, you will create a
# program that removes all of the comments from a Python source file. Check each
# line in the file to determine if a # character is present. If it is then your program
# should remove all of the characters from the # character to the end of the line (we’ll
# ignore the situation where the comment character occurs inside of a string). Save the
# modified file using a new name that will be entered by the user. The user will also
# enter the name of the input file. Ensure that an appropriate error message is displayed
# if a problem is encountered while accessing the files.

# solution

# Exercise 150: Remove Comments from a Python File

while True:
    try:
        # 🔹 Ask user for input file name
        input_filename = input(
            "Enter the name of the Python file to clean (e.g., code.py): ").strip()

        if input_filename == "":
            print("File name cannot be empty. Please try again.\n")
            continue

        # 🔹 Ask user for output file name
        output_filename = input(
            "Enter the new name to save the cleaned file (e.g., no_comments.py): ").strip()

        if output_filename == "":
            print("Output file name cannot be empty. Please try again.\n")
            continue

        # 🔹 Try opening the input file
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            for line in infile:
                # If there is a # symbol, keep only text before it
                if '#' in line:
                    cleaned_line = line.split(
                        '#')[0].rstrip()  # remove comment
                    outfile.write(cleaned_line + "\n")  # write cleaned line
                else:
                    outfile.write(line)  # no comment → write normally

        print(
            f"\nComments removed successfully! New file saved as: {output_filename}")
        break  # Exit the loop after success

    except FileNotFoundError:
        print("\n❌ Error: The input file was not found. Please check the name and try again.\n")

    except PermissionError:
        print("\n❌ Error: You do not have permission to read/write this file.\n")

    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}\n")
