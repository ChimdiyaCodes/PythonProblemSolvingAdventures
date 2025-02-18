# Exercise 17: Heat Capacity

# The amount of energy required to increase the temperature of one gram of a material
# by one degree Celsius is the material’s specific heat capacity, C. The total amount
# of energy required to raise m grams of a material by ΔT degrees Celsius can be
# computed using the formula:
# q = mCΔT.
# Write a program that reads the mass of some water and the temperature change
# from the user. Your program should display the total amount of energy that must be
# added or removed to achieve the desired temperature change.
# Extend your program so that it also computes the cost of heating the water. Elec￾tricity is normally billed using units of kilowatt hours rather than Joules. In this
# exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
# your program to compute the cost of boiling water for a cup of coffee.

# Solution:

while True:
    try:
        # take input from user
        mass_of_water = float(input("\nEnter the mass of water in g or ml: "))
        temperature_change = float(
            input("\nEnter the change in temperature in degree celsius: "))

        # Validate inputs
        if mass_of_water <= 0 or temperature_change <= 0:
            print("Mass and temperature change must be positive values.")
            continue

        # calculate the energy and cost of heating
        c = 4.186
        q = mass_of_water * c * temperature_change
        energy_in_kWh = q / 3600000
        cost_per_kWh = 8.9
        cost_of_heating = energy_in_kWh * cost_per_kWh

        # print the results
        print(
            f"\nThe energy required in joules to raise {mass_of_water}g of water by {temperature_change}\u00B0C is {q:.2f}J")
        print(
            f"\nThe cost of electricity required for the heating is {cost_of_heating:.2f}cents")

        while True:
            calculate_again = input(
                """\nWould you like to make another calculation? : 
                    \nEnter \n\nY for YES \n\nN for NO: """).upper()
            if calculate_again in ['Y', 'YES', 'N', 'NO']:
                break
            print("Invalid input! Please enter Y or N.")

        if calculate_again in ['N', 'NO']:
            print("\nThank you for using the calculator!")
            break

    except ValueError:
        print("Invalid input. Please enter a numeric value.")
