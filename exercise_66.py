# Exercise 66: Compute a Grade Point Average

# Exercise 51 included a table that shows the conversion from letter grades to grade
# points at a particular academic institution. In this exercise you will compute the
# grade point average of an arbitrary number of letter grades entered by the user. The
# user will enter a blank line to indicate that all of the grades have been provided. For
# example, if the user enters A, followed by C+, followed by B, followed by a blank
# line then your program should report a grade point average of 3.1.
# You may find your solution to Exercise 51 helpful when completing this exercise.
# Your program does not need to do any error checking. It can assume that each value
# entered by the user will always be a valid letter grade or a blank line.

# solution:

# step 1: define the grade to point mapping

grade_to_points = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0.0
}

# step 2: collect grades from the user

grades = []
while True:
    grade = input(
        "\nEnter a letter grade (or blank to quit): ").strip().upper()
    if grade == "":
        break  # exit  the loop if the user enters a blank line
    grades.append(grade)

# step 3: convert grades to points
total_points = 0
for grade in grades:
    total_points += grade_to_points.get(grade, 0.0)  # look up the grade point

# step 4: calculate the gpaa

if len(grades) > 0:
    gpa = total_points / len(grades)

else:
    gpa = 0.0  # Handle the case where no grades are entered

# Step 5: Display the result
print(f"\nThe Grade Point Average (GPA) is: {gpa:.1f}")
