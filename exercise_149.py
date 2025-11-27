# Exercise 149: Both Letter Grades and Grade Points

# Write a program that converts from letter grades to grade points and vice-versa.
# Your program will convert multiple values entered by the user, with one value
# entered on each line. Begin by attempting to convert each value entered by the
# user from a number of grade points to a letter grade. If an exception occurs during the attempt then your program should attempt to convert the value from a letter grade to a number of grade points. If both conversions fail then your program
# should provide a message indicating that the supplied input is invalid. Design your
# program so that it continues performing conversions until the user enters a blank
# line. Your solutions to Exercises 51 and 52 may be helpful when completing this
# exercise.

# solution

# Dictionary for letter grade to grade points (Exercise 51 logic)
letter_to_points = {
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

# List of tuples for grade points to letter grade (Exercise 52 logic)
# Ordered from highest to lowest for easier comparison
points_to_letter = [
    (4.0, "A+"),
    (3.7, "A"),
    (3.3, "A-"),
    (3.0, "B+"),
    (2.7, "B"),
    (2.3, "B-"),
    (2.0, "C+"),
    (1.7, "C"),
    (1.3, "C-"),
    (1.0, "D+"),
    (0.7, "D"),
    (0.0, "F")
]

print("\nEnter letter grades or grade points.")
print("Example: A-, B+, 3.5, 2.7 etc.")
print("Press Enter on a blank line to exit.\n")

while True:
    user_input = input("Enter a value to convert: ").strip()

    # Exit condition
    if user_input == "":
        print("\nProgram ended.")
        break

    # STEP 1: Try treat input as grade points (number)
    try:
        grade_point = float(user_input)  # Try converting to a float

        # If number is 4.0 or above, it's automatically A+
        if grade_point >= 4.0:
            print(f"→ Letter Grade: A+")
            continue

        # Find closest letter grade
        closest_grade = None
        min_difference = float('inf')

        for lower_bound, letter_grade in points_to_letter:
            difference = abs(grade_point - lower_bound)
            if difference < min_difference:
                min_difference = difference
                closest_grade = letter_grade

        print(f"→ Letter Grade: {closest_grade}")

    except ValueError:
        # STEP 2: Try treat input as letter grade (mapping lookup)
        letter = user_input.upper()

        if letter in letter_to_points:
            print(f"→ Grade Points: {letter_to_points[letter]}")
        else:
            # STEP 3: If both fail → input invalid
            print("❌ Invalid input. Try again.")
