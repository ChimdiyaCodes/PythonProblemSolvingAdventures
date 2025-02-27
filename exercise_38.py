# Exercise 38: Month Name to Number of Days

# The length of a month varies from 28 to 31 days. In this exercise you will create
# a program that reads the name of a month from the user as a string. Then your
# program should display the number of days in that month. Display “28 or 29 days”
# for February so that leap years are addressed.

# solution

while True:  # keeps prompting user for input until a valid input is entered

    # Prompt the user to enter the name of a month

    month_name = input("\nEnter the name of a month: ").strip().title()

    # Determine the number of days in the month

    if month_name == "February":
        days = "28 or 29 days"  # account for leap years
    elif month_name in ("April" "June", "September", "November"):
        days = "30 days"
    elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
        days = "31 days"
    else:
        # Handle invalid input
        print(
            "Error: Invalid month name. Please enter a valid month in full spelling.")
        continue  # reprompt the user for input

    # Display the result
    print(f"\n{month_name} has {days}.")
    break  # exit loop
