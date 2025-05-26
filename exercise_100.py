# Exercise 100: Days in a Month

# Write a function that determines how many days there are in a particular month. Your
# function will take two parameters: The month as an integer between 1 and 12, and
# the year as a four digit integer. Ensure that your function reports the correct number
# of days in February for leap years. Include a main program that reads a month and
# year from the user and displays the number of days in that month. You may find your
# solution to Exercise 57 helpful when solving this problem.

# solution

def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def days_in_month(month, year):
    """Return number of days in the given month and year."""
    if month == 2:  # February
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    else:  # January, March, May, July, August, October, December
        return 31


def main():
    while True:
        try:
            month = int(input("\nEnter the month (1-12): "))
            if month < 1 or month > 12:
                raise ValueError("Month must be between 1 and 12.")

            year = int(input("\nEnter the year (e.g., 2024): "))
            if year < 1 or len(str(year)) != 4:
                raise ValueError("Year must be a 4-digit positive number.")

            days = days_in_month(month, year)
            print(f"\nThere are {days} days in month {month} of year {year}.")
            break  # Exit the loop if everything is valid

        except ValueError as ve:
            print("Invalid input:", ve)
        except Exception as e:
            print("An unexpected error occurred:", e)


# Run the main program
if __name__ == "__main__":
    main()
