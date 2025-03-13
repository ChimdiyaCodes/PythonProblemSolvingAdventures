# Exercise 63: Temperature Conversion Table

# Write a program that displays a temperature conversion table for degrees Celsius and
# degrees Fahrenheit. The table should include rows for all temperatures between 0
# and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
# headings on your columns. The formula for converting between degrees Celsius and
# degrees Fahrenheit can be found on the internet.

# solution

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.
    Formula: F = (9/5) * C + 32
    """
    return (9 / 5) * celsius + 32


def display_temperature_table():
    """
    Display a temperature conversion table for Celsius to Fahrenheit.
    The table includes temperatures from 0°C to 100°C in steps of 10°C.
    """
    # Print the table header
    print(f"{'Celsius (°C)':<15} {'Fahrenheit (°F)':<15}")
    print("-" * 30)

    # Loop through temperatures from 0°C to 100°C in steps of 10°C
    for celsius in range(0, 101, 10):
        fahrenheit = celsius_to_fahrenheit(celsius)
        # Print the formatted row
        print(f"{celsius:<15} {fahrenheit:<15.2f}")


display_temperature_table()
