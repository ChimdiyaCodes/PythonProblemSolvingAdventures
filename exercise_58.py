# Exercise 58: Next Day

# Write a program that reads a date from the user and computes its immediate successor.
# For example, if the user enters values that represent 2013-11-18 then your program
# should display a message indicating that the day immediately after 2013-11-18 is
# 2013-11-19. If the user enters values that represent 2013-11-30 then the program
# should indicate that the next day is 2013-12-01. If the user enters values that represent
# 2013-12-31 then the program should indicate that the next day is 2014-01-01. The
# date will be entered in numeric form with three separate input statements; one for
# the year, one for the month, and one for the day. Ensure that your program works
# correctly for leap years.

# solution:

def is_leap_year(year):
    """
    Determine if a given year is a leap year.

    """
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    """
    Return the number of days in a given month and year.

    """
    if month == 2:  # February
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        return 30
    else:  # January, March, May, July, August, October, December
        return 31


def get_next_date(year, month, day):
    """
    Compute the next day for a given date.

    """
    # Check if the current day is the last day of the month
    if day == days_in_month(year, month):
        day = 1
        # Check if the current month is December
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    else:
        day += 1

    return year, month, day


def main():
    """
    Main function to handle user input and compute the next day.
    """
    print("\nWelcome To The Next Day Calculator!")
    print("------------------")

    while True:
        try:
            # Get user input for year, month, and day
            year = int(input("\nEnter the year: "))
            month = int(input("\nEnter the month (1-12): "))
            day = int(input("\nEnter the day: "))

            # Validate the input
            if year < 1:
                print("Year must be a positive integer. Please try again.")
                continue
            if month < 1 or month > 12:
                print("Month must be between 1 and 12. Please try again.")
                continue
            if day < 1 or day > days_in_month(year, month):
                print("Invalid day for the given month and year. Please try again.")
                continue

            # Compute the next day
            next_year, next_month, next_day = get_next_date(year, month, day)

            # Display the result
            print(
                f"\nThe next day after {year}-{month:02d}-{day:02d} is {next_year}-{next_month:02d}-{next_day:02d}.")
            break

        except ValueError:
            print("Invalid input. Please enter integers for year, month, and day.")


if __name__ == "__main__":
    main()
