# Exercise 30: Units of Pressure

# In this exercise you will create a program that reads a pressure from the user in kilopascals. Once the pressure has been read your program should report the equivalent
# pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
# your research skills to determine the conversion factors between these units.

# Solution:

# Constants for conversion factors
KPA_TO_PSI = 0.145038
KPA_TO_MMHG = 7.50062
KPA_TO_ATM = 0.00986923

while True:
    try:
        # Take input
        pressure_in_kpa = float(input("\nEnter your pressure in kPa: "))

        # Perform conversions
        pressure_in_psi = round(pressure_in_kpa * KPA_TO_PSI, 2)
        pressure_in_mmHg = round(pressure_in_kpa * KPA_TO_MMHG, 2)
        pressure_in_atm = round(pressure_in_kpa * KPA_TO_ATM, 2)

        # Display results
        print(f"""\n{pressure_in_kpa} kPa converted to:
Pounds per square inch = {pressure_in_psi} psi
Millimetres of mercury = {pressure_in_mmHg} mmHg
Atmospheres = {pressure_in_atm} atm
        """)

        # Ask if the user wants to perform another conversion
        another_conversion = input(
            "Do you want to convert another value? (yes/no): ").lower()
        if another_conversion != "yes":
            print("Thank you for using the calculator!")
            break
    except ValueError:
        print("Invalid input! Please enter a numeric value in kilopascals (kPa).")
