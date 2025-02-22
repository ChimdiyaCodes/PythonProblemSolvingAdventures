# Exercise 28:Wind Chill

# When the wind blows in cold weather, the air feels even colder than it actually is
# because the movement of the air increases the rate of cooling for warm objects, like
# people. This effect is known as wind chill.
# In 2001, Canada, the United Kingdom and the United States adopted the following formula for computing the wind chill index. Within the formula Ta is the
# air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
# A similar formula with different constant values can be used with temperatures in
# degrees Fahrenheit and wind speeds in miles per hour.
# WCI = 13.12 + 0.6215Ta − 11.37V0.16 + 0.3965TaV0.16
# Write a program that begins by reading the air temperature and wind speed from the
# user. Once these values have been read your program should display the wind chill
# index rounded to the closest integer.
# The wind chill index is only considered valid for temperatures less than or
# equal to 10 degrees Celsius and wind speeds exceeding 4.8 kilometers per
# hour.


# Function to calculate Wind Chill Index (WCI)
def calculate_wci(temperature, wind_speed):
    return 13.12 + (0.6215 * temperature) - (11.37 * (wind_speed ** 0.16)) + (0.3965 * temperature * (wind_speed ** 0.16))

# Function to validate input constraints


def is_valid_input(temperature, wind_speed):
    return temperature <= 10 and wind_speed > 4.8

# Main program


def main():
    # Read air temperature and wind speed from the user
    try:
        temperature = float(
            input("Enter the air temperature in degrees Celsius: "))
        wind_speed = float(
            input("Enter the wind speed in kilometers per hour: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Check if the input values are valid for WCI calculation
    if not is_valid_input(temperature, wind_speed):
        print("Wind Chill Index is only valid for temperatures <= 10°C and wind speeds > 4.8 km/h.")
        return

    # Calculate the Wind Chill Index
    wci = calculate_wci(temperature, wind_speed)

    # Display the result rounded to the nearest integer
    print(f"The Wind Chill Index is: {round(wci)}")


# Run the program
if __name__ == "__main__":
    main()
