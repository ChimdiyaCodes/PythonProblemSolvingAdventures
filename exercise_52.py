# Exercise 52: Grade Points to Letter Grade

# In the previous exercise you created a program that converts a letter grade into the
# equivalent number of grade points. In this exercise you will create a program that
# reverses the process and converts from a grade point value entered by the user to a
# letter grade. Ensure that your program handles grade point values that fall between
# letter grades. These should be rounded to the closest letter grade. Your program
# should report A+ for a 4.0 (or greater) grade point average.

# solution:

def grade_points_to_letter_grade():
    # Mapping of grade point ranges to letter grades
    grade_mapping = [
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

    while True:
        try:
            # Prompt the user for input
            grade_point = float(
                input("\nEnter your grade point value (0.0 to 4.0): "))

            # Validate the input range
            if grade_point < 0.0 or grade_point > 4.0:
                print("Invalid grade point. Please enter a value between 0.0 and 4.0.")
                continue  # Skip the rest of the loop and prompt again

            # Handle A+ case (4.0 or greater)
            if grade_point >= 4.0:
                print(f"\nThe letter grade for {grade_point} is: A+")
                break  # Exit the loop after valid input

            # Find the closest letter grade
            closest_grade = None
            min_difference = float('inf')  # Initialize with a large value

            for lower_bound, letter_grade in grade_mapping:
                difference = abs(grade_point - lower_bound)
                if difference < min_difference:
                    min_difference = difference
                    closest_grade = letter_grade

            # Output the result
            print(f"\nThe letter grade for {grade_point} is: {closest_grade}")
            break  # Exit the loop after valid input

        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a numeric value.")


# Run the function
grade_points_to_letter_grade()
