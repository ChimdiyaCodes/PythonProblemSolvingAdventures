# Exercise 29: Celsius to Fahrenheit and Kelvin

# Write a program that begins by reading a temperature from the user in degrees
# Celsius. Then your program should display the equivalent temperature in degrees
# Fahrenheit and degrees Kelvin. The calculations needed to convert between different
# units of temperature can be found on the internet.

# Solution
# Function to convert Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Celsius to Kelvin


def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Function to get a valid temperature input from the user


def get_temperature_input():
    while True:
        try:
            temperature = float(input("\nEnter the temperature in Celsius: "))
            if -273.15 <= temperature <= 10000:
                return temperature
            else:
                print(
                    "Temperature must be between -273.15°C and 10,000°C. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Main program


def main():
    while True:
        # Get temperature input from the user
        temp_in_celsius = get_temperature_input()

        # Convert temperature to Fahrenheit and Kelvin
        temp_in_fahrenheit = celsius_to_fahrenheit(temp_in_celsius)
        temp_in_kelvin = celsius_to_kelvin(temp_in_celsius)

        # Display the results
        print(f"\n{temp_in_celsius}°C is equal to:")
        print(f"- {temp_in_fahrenheit:.2f}°F")
        print(f"- {temp_in_kelvin:.2f}K")

        # Ask the user if they want to make another calculation
        while True:
            convert_again = input(
                """\nWould you like to make another conversion? : 
                                \nEnter \n\nY for YES \n\nN for NO: """).upper()
            if convert_again in ['Y', 'YES', 'N', 'NO']:
                break
            print("Invalid input! Please enter Y or N.")

        # Exit the loop if the user does not want to continue
        if convert_again in ['N', 'NO']:
            print("\nThank you for using the temperature converter!")
            break


# Run the program
if __name__ == "__main__":
    main()
