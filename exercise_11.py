# Exercise 11: Fuel Efficiency

# In the United States, fuel efficiency for vehicles is normally expressed in miles-per gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
# kilometers (L/100 km). Use your research skills to determine how to convert from
# MPG to L/100 km. Then create a program that reads a value from the user in American
# units and displays the equivalent fuel efficiency in Canadian units

# Solution:

# Take input from the user
while True:
    try:
        mpg = float(
            input("\nEnter your fuel efficiency in miles per gallon (MPG): "))

        # Check for valid MPG value
        if mpg <= 0:
            print("Fuel efficiency must be a positive number.")
            continue

        # Convert MPG to L/100KM
        mpg_conversion = round(235.214583 / mpg)

        # Display the results
        print(f"\n{mpg} MPG is equivalent to {mpg_conversion:.2f} L/100KM.")

        while True:
            convert_again = input(
                """\nWould you like to make another conversion? : 
    \nEnter \n\nY for YES \n\nN for No: """)
            if convert_again in ['Y', 'y', 'YES', 'yes']:
                break  # Break the inner loop to do another calculation
            elif convert_again in ['N', 'n', 'NO', 'no']:
                print("\nThank you for using the converter!")
                exit()  # Exit the program
            else:
                print("\nInvalid input! Please enter Y for yes or N for no.")
                continue  # Keep asking for valid input

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
