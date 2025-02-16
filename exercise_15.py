# Exercise 15: Distance Units

# In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles.

# Solution:

while True:
    try:
        # taking input from the user

        distance_in_ft = int(input("\nEnter your distance in feet: "))

        # convert feet to inches

        feet_to_inches = distance_in_ft * 12

        # convert feet to yards

        feet_to_yards = distance_in_ft / 3

        # convert feet to miles

        feet_to_miles = distance_in_ft / 5280

        # display final results

        print(f"\n{distance_in_ft} feet is equivalent to: \n\n"
              f"- {feet_to_inches:,.2f} inches \n"
              f"- {feet_to_yards:,.2f} yards \n"
              f"- {feet_to_miles:,.6f} miles")

        while True:
            convert_again = input(
                """\nWould you like to make another conversion? : 
                    \nEnter \n\nY for YES \n\nN for NO: """).upper()
            if convert_again in ['Y', 'YES', 'N', 'NO']:
                break
            print("Invalid input! Please enter Y or N.")

        if convert_again in ['N', 'NO']:
            print("\nThank you for using the converter!")
            break

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
