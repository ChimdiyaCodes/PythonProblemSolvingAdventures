# Exercise 47: Birth Date to Astrological Sign

# The horoscopes commonly reported in newspapers use the position of the sun at the
# time of one’s birth to try and predict the future. This system of astrology divides the
# year into twelve zodiac signs, as outline in the table below:
# Zodiac sign Date range
# Capricorn December 22 to January 19
# Aquarius January 20 to February 18
# Pisces February 19 to March 20
# Aries March 21 to April 19
# Taurus April 20 to May 20
# Gemini May 21 to June 20
# Cancer June 21 to July 22
# Leo July 23 to August 22
# Virgo August 23 to September 22
# Libra September 23 to October 22
# Scorpio October 23 to November 21
# Sagittarius November 22 to December 21
# Write a program that asks the user to enter his or her month and day of birth. Then
# your program should report the user’s zodiac sign as part of an appropriate output
# message.

# solution

def get_zodiac_sign(month, day):
    """
    Determines the zodiac sign based on the given month and day.
    """
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    else:
        return "Invalid date"


def is_valid_date(month, day):
    """
    Checks if the given month and day form a valid date.
    """
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    # Check months with 30 days
    if month in {4, 6, 9, 11} and day > 30:
        return False
    # Check February
    if month == 2 and day > 29:
        return False
    return True


def main():
    """
    Main function to run the program.
    """
    print("\nWelcome to the Astrological Sign Finder!")

    while True:
        try:
            # Get user input
            month = int(input("\nEnter your birth month (1-12): "))
            day = int(input("\nEnter your birth day (1-31): "))

            # Validate the date
            if not is_valid_date(month, day):
                print("Invalid date. Please enter a valid month and day.")
                continue

            # Determine and display the zodiac sign
            zodiac_sign = get_zodiac_sign(month, day)
            if zodiac_sign == "Invalid date":
                print("Invalid date. Please try again.")
            else:
                print(f"\nYour zodiac sign is {zodiac_sign}.")
                break

        except ValueError:
            print("Invalid input. Please enter numeric values for month and day.")


if __name__ == "__main__":
    main()
