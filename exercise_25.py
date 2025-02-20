# Exercise 25: Units of Time (Again)

# In this exercise you will reverse the process described in the previous exercise.
# Develop a program that begins by reading a number of seconds from the user.
# Then your program should display the equivalent amount of time in the form
# D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively. The hours, minutes and seconds should all be formatted so that
# they occupy exactly two digits, with a leading 0 displayed if necessary

# Solution

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


# Get total seconds from user
total_seconds = correct_integer("\nEnter the number of seconds: ")

# Calculate days, hours, minutes, and seconds
seconds_per_day = 24 * 60 * 60
seconds_per_hour = 60 * 60
seconds_per_minute = 60

# Extract days
days = total_seconds // seconds_per_day
remaining_seconds = total_seconds % seconds_per_day

# Extract hours
hours = remaining_seconds // seconds_per_hour
remaining_seconds = remaining_seconds % seconds_per_hour

# Extract minutes
minutes = remaining_seconds // seconds_per_minute
seconds = remaining_seconds % seconds_per_minute

# Format output as D:HH:MM:SS
print(f"""
{days}:{hours:02d}:{minutes:02d}:{seconds:02d}
\nmeaning that in {total_seconds} seconds, there are: 
         {days} days
         {hours} hours
         {minutes} minutes
         {seconds} seconds
""")
