# Exercise 20: Ideal Gas Law
#
# The ideal gas law is a mathematical approximation of the behavior of gasses as
# pressure, volume and temperature change. It is usually stated as:
# PV = nRT
# where P is the pressure in Pascals, V is the volume in liters, n is the amount of
# substance in moles, R is the ideal gas constant, equal to 8.314 mol K
# J , and T is the
# temperature in degrees Kelvin.
# Write a program that computes the amount of gas in moles when the user supplies
# the pressure, volume and temperature. Test your program by determining the number
# of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
# a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is
# approximately 20 degrees Celsius or 68 degrees Fahrenheit.

# Solution:

IDEAL_GAS_CONSTANT = 8.314  # J/(mol·K)

while True:
    try:
        # Prompt for inputs
        pressure = float(input("\nEnter the pressure (in Pascal): "))
        if pressure <= 0:
            print("Pressure must be positive")
            continue

        volume = float(input("\nEnter the volume (in liters): "))
        if volume <= 0:
            print("Volume must be positive")
            continue

        temperature = float(
            input("\nEnter the temperature (will specify unit next): "))
        unit = input(
            "Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

        if unit not in ['c', 'f']:
            print("Please enter 'C' or 'F' for the temperature unit")
            continue

        # Convert to Kelvin
        if unit == 'c':
            temp_in_kelvin = temperature + 273.15
        else:  # unit == 'f'
            temp_in_kelvin = (temperature - 32) * 5/9 + 273.15

        # Check for physically meaningful temperature
        if temp_in_kelvin <= 0:
            print("Temperature cannot be below absolute zero (-273.15°C or -459.67°F)")
            continue

        # Calculate moles
        n = (pressure * volume) / (IDEAL_GAS_CONSTANT * temp_in_kelvin)

        # Display results
        print(f"\nResults:")
        print(f"Temperature in Kelvin: {temp_in_kelvin:.2f} K")
        print(f"Amount of gas in moles: {n:.2f} moles")
        break

    except ValueError:
        print("Invalid input. Please enter numeric values only.")
