# Exercise 51: Letter Grade to Grade Points

# At a particular university, letter grades are mapped to grade points in the following
# manner:
# Letter Grade points
# A+ 4.0
# A 4.0
# A− 3.7
# B+ 3.3
# B 3.0
# B− 2.7
# C+ 2.3
# C 2.0
# C− 1.7
# D+ 1.3
# D 1.0
# F 0
# Write a program that begins by reading a letter grade from the user. Then your
# program should compute and display the equivalent number of grade points. Ensure
# that your program generates an appropriate error message if the user enters an invalid
# letter grade.

# solution:

def letter_grade_to_grade_points():
    # Mapping of letter grades to grade points
    grade_mapping = {
        'A+': 4.0,
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D+': 1.3,
        'D': 1.0,
        'F': 0.0
    }

    while True:
        # Prompt the user for input
        letter_grade = input(
            "\nEnter your letter grade (e.g., A+, B-, C): ").strip().upper()

        # Check if the input is in the mapping
        if letter_grade in grade_mapping:
            # Retrieve the corresponding grade points
            grade_points = grade_mapping[letter_grade]
            print(f"\nThe grade points for {letter_grade} are: {grade_points}")
            break  # Exit the loop after valid input
        else:
            # Display an error message for invalid input
            print(
                "Invalid letter grade. Please enter a valid letter grade (e.g., A+, B-, C).")


# Run the function
letter_grade_to_grade_points()
