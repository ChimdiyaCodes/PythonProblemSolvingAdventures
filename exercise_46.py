# Exercise 46: Season from Month and Day

# The year is divided into four seasons: spring, summer, fall and winter. While the
# exact dates that the seasons change vary a little bit from year to year because of the
# way that the calendar is constructed, we will use the following dates for this exercise:
# Season First day
# Spring March 20
# Summer June 21
# Fall September 22
# Winter December 21
# Create a program that reads a month and day from the user. The user will enter
# the name of the month as a string, followed by the day within the month as an
# integer. Then your program should display the season associated with the date that
# was entered.

# solution

print("\nWelcome! This season checker takes a month and day and tells you the season (spring, summer, fall and winter).")


def valid_month(month):
    """Check if the month is valid."""
    valid_months = [
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
    ]
    return month.lower() in valid_months


def valid_day(month, day):
    """Check if the day is valid for the given month."""
    if month.lower() in ["april", "june", "september", "november"]:
        return 1 <= day <= 30
    elif month.lower() == "february":
        return 1 <= day <= 29  # Assuming leap years are not considered
    else:
        return 1 <= day <= 31


def get_season(month, day):
    """Determine the season based on the month and day."""
    month = month.lower()
    if (month == "march" and day >= 20) or (month == "april") or (month == "may") or (month == "june" and day < 21):
        return "Spring"
    elif (month == "june" and day >= 21) or (month == "july") or (month == "august") or (month == "september" and day < 22):
        return "Summer"
    elif (month == "september" and day >= 22) or (month == "october") or (month == "november") or (month == "december" and day < 21):
        return "Fall"
    else:
        return "Winter"


# Main program
while True:
    try:
        # Read the month and day from the user
        month = input("\nEnter the month (e.g., March, June, etc.): ").strip()
        day = int(input("\nEnter the day: ").strip())

        # Validate the month
        if not valid_month(month):
            print(
                "Error: Invalid month. Please enter a valid month (e.g., March, June, etc.).")
            continue

        # Validate the day
        if not valid_day(month, day):
            print(
                f"Error: Invalid day for {month.capitalize()}. Please enter a valid day.")
            continue

        # Determine the season
        season = get_season(month, day)

        # Output the result
        print(f"The season for {month.capitalize()} {day} is {season}.")
        break  # Exit the loop if the input is valid
    except ValueError:
        print("Error: Invalid input. Please enter a valid day as an integer.")
