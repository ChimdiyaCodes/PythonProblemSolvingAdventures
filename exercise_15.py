# Exercise 15: Distance Units

# In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles. Use the Internet to look up the necessary conversion factors
# if you don’t have them memorized.

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
                    \nEnter \n\nY for YES \n\nN for NO: """)
            if convert_again.upper() in ['Y', 'YES']:
                break  # Break the inner loop to do another calculation
            elif convert_again.upper() in ['N', 'NO']:
                print("\nThank you for using the converter!")
                exit()  # Exit the function (and program)
            else:
                print("\nInvalid input! Please enter Y for yes or N for no.")
                continue  # Keep asking for valid input

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
