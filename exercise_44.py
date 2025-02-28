# Exercise 44: Date to Holiday Name

# Canada has three national holidays which fall on the same dates each year.
# Holiday Date
# New year’s day January 1
# Canada day July 1
# Christmas day December 25
# Write a program that reads a month and day from the user. If the month and day
# match one of the holidays listed previously then your program should display the
# holiday’s name. Otherwise your program should indicate that the entered month and
# day do not correspond to a fixed-date holiday.
# Canada has two additional national holidays, Good Friday and Labour Day,
# whose dates vary from year to year. There are also numerous provincial and
# territorial holidays, some of which have fixed dates, and some of which have
# variable dates. We will not consider any of these additional holidays in this
# exercise.

# solution

print("\nWelcome to the Canadian Holiday Checker!")
print("This program checks if a given date corresponds to a fixed-date national holiday in Canada.")


def get_holiday_name(month, day):
    """Returns the name of the holiday if the date matches, otherwise returns none."""
    if month == 1 and day == 1:
        return "New Year's Day"
    elif month == 7 and day == 1:
        return "Canada Day"
    elif month == 12 and day == 25:
        return "Christmas Day"
    else:
        return None


def valid_date(month, day):
    """Checks if the given month and day form a valid date."""
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    # Check for months with 30 days
    if month in {4, 6, 9, 11} and day > 30:
        return False
    # Check for February
    if month == 2 and day > 29:
        return False
    return True


def main():
    while True:
        try:
            # get input from the user
            month = int(input("\nEnter the month (1-12): "))
            day = int(input("\nEnter the day (1-31): "))

            # validate the date
            if not valid_date(month, day):
                print("Invalid date. Please enter a valid month and day.")
                continue

            # get the holiday name
            holiday_name = get_holiday_name(month, day)

            # display the result
            if holiday_name:
                print(
                    f"\nThe date {month}/{day} corresponds to {holiday_name}.")
                break
            else:
                print(
                    f"The date {month}/{day} does not correspond to a fixed-date holiday.")
            while True:
                calculate_again = input(
                    """\nWould you like to get another holiday? : 
                            \nEnter \n\nY for YES \n\nN for NO: """).upper()
                if calculate_again in ['Y', 'YES', 'N', 'NO']:
                    break
                print("Invalid input! Please enter Y or N.")

            if calculate_again in ['N', 'NO']:
                print("\nThank you, bye!")
                break
        except ValueError:
            print("Invalid input. Please enter numeric values for month and day.")


if __name__ == "__main__":
    main()
