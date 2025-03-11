# Exercise 57: Is it a Leap Year?

# Most years have 365 days. However, the time required for the Earth to orbit the Sun
# is actually slightly more than that. As a result, an extra day, February 29, is included
# in some years to correct for this difference. Such years are referred to as leap years.
# The rules for determining whether or not a year is a leap year follow:
# • Any year that is divisible by 400 is a leap year.
# • Of the remaining years, any year that is divisible by 100 is not a leap year.
# • Of the remaining years, any year that is divisible by 4 is a leap year.
# • All other years are not leap years.
# Write a program that reads a year from the user and displays a message indicating
# whether or not it is a leap year.

# solution:

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def main():
    """
    Main function to handle user input and display whether a year is a leap year.
    """
    print("\nWelcome to The Leap Year Checker")
    print("-----------------")

    while True:
        try:
            # Get user input
            year = int(input("\nEnter a year (or type '0' to exit): "))

            # Exit condition
            if year == 0:
                print("Thank you for using the leap year checker. Goodbye!")
                break

            # Validate input
            if year < 0:
                print("Please enter a valid year (greater than 0).")
                continue

            # Check if it's a leap year
            if is_leap_year(year):
                print(f"\n{year} is a leap year.")
            else:
                print(f"\n{year} is not a leap year.")

        except ValueError:
            print("Invalid input. Please enter a valid integer year.")


if __name__ == "__main__":
    main()
