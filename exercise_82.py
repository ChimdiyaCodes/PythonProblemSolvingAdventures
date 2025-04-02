# Exercise 82: Taxi Fare

# In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25
# for every 140 meters traveled. Write a function that takes the distance traveled (in
# kilometers) as its only parameter and returns the total fare as its only result. Write a
# main program that demonstrates the function.
# Hint: Taxi fares change over time. Use constants to represent the base fare and
# the variable portion of the fare so that the program can be updated easily when
# the rates increase.

# solution:

import math

# Constants for easy maintenance
BASE_FARE = 4.00  # in dollars
RATE_PER_140M = 0.25  # in dollars
METER_RATE_UNIT = 140  # meters


def calculate_taxi_fare(distance_km):
    """
    Calculate taxi fare based on distance traveled.

    Parameters:
    distance_km (float): Distance traveled in kilometers

    Returns:
    float: Total fare in dollars
    """
    # Convert km to meters
    distance_meters = distance_km * 1000

    # Calculate number of 140-meter units (rounded up)
    units = math.ceil(distance_meters / METER_RATE_UNIT)

    # Calculate total fare
    variable_fare = units * RATE_PER_140M
    total_fare = BASE_FARE + variable_fare

    return total_fare


def get_positive_number(prompt):
    """
    Continuously prompt the user until a valid positive number is entered.

    Parameters:
    prompt (str): The message to display to the user

    Returns:
    float: The valid positive number entered by the user
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please, enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("\nTaxi Fare Calculator")
    print("------------------------")

    # Get valid distance input
    distance = get_positive_number("Enter distance traveled in kilometers: ")

    # Calculate fare
    fare = calculate_taxi_fare(distance)

    # Display result
    print(f"\nTaxi fare for {distance:.2f} km: ${fare:.2f}")


if __name__ == "__main__":
    main()
