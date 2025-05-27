# Exercise 103: Magic Dates

# A magic date is a date where the day multiplied by the month is equal to the two digit
# year. For example, June 10, 1960 is a magic date because June is the sixth month, and
# 6 times 10 is 60, which is equal to the two digit year. Write a function that determines
# whether or not a date is a magic date. Use your function to create a main program
# that finds and displays all of the magic dates in the 20th century. You will probably
# find your solution to Exercise 100 helpful when completing this exercise.

# solution

from datetime import date, timedelta


def is_magic_date(dt):
    # Check if a date is magic (month * day == last two digits of year).
    day = dt.day
    month = dt.month
    year = dt.year % 100  # Get last 2 digits
    return day * month == year


def find_magic_dates(start_year=1900, end_year=1999):
    # Find all magic dates between two years.
    magic_dates = []

    # Start from Jan 1 of start_year
    current = date(start_year, 1, 1)

    # End at Dec 31 of end_year
    end = date(end_year, 12, 31)

    # Loop one day at a time
    while current <= end:
        if is_magic_date(current):
            magic_dates.append(current.strftime("%B %d, %Y"))  # Format nicely
        current += timedelta(days=1)

    return magic_dates


def main():
    print("Magic Dates in the 20th Century:")
    magic_dates = find_magic_dates()
    for magic in magic_dates:
        print(magic)


if __name__ == "__main__":
    main()
