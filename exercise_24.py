# Exercise 24: Units of Time

# Create a program that reads a duration from the user as a number of days, hours,
# minutes, and seconds. Compute and display the total number of seconds represented
# by this duration.

# Solution:

# function for input validation
def correct_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


# Take input from the user
days = correct_integer("\nEnter the number of days: ")
hours = correct_integer("\nEnter the number of hours (0-23): ")
minutes = correct_integer("\nEnter the number of minutes (0-59): ")
seconds = correct_integer("\nEnter the number of seconds (0-59): ")

# Convert each unit to seconds
days_to_secs = days * 24 * 60 * 60
hours_to_secs = hours * 60 * 60
mins_to_secs = minutes * 60

# Sum the results
total_secs = days_to_secs + hours_to_secs + mins_to_secs + seconds

# Display result
print(f"""\nThe total number of seconds contained in:
{days} days
{hours} hours
{minutes} minutes and
{seconds} seconds
is equal to {total_secs} seconds
""")
