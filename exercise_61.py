# Exercise 61: Average

# In this exercise you will create a program that computes the average of a collection
# of values entered by the user. The user will enter 0 as a sentinel value to indicate
# that no further values will be provided. Your program should display an appropriate
# error message if the first value entered by the user is 0.
# Hint: Because the 0 marks the end of the input it should not be included in the
# average.

# solution

def calculate_average():
    # Initialize variables
    total_sum = 0  # To store the sum of all numbers
    count = 0      # To store the count of numbers entered

    print("\nWelcome to The Average calculator!")
    print("You will be prompted to enter the numbers whose average you want to calculate one after the other below")

    while True:
        try:
            # Prompt the user for input

            user_input = input("\nEnter a number (0 to stop): ")

            # Convert input to a float
            number = float(user_input)

            # Check if the first input is 0
            if count == 0 and number == 0:
                print(
                    "Error: The first value cannot be 0. Please enter at least one number.")
                continue

            # If the user enters 0, exit the loop
            if number == 0:
                break

            # Add the number to the total sum and increment the count
            total_sum += number
            count += 1

        except ValueError:
            # Handle invalid inputs (e.g., non-numeric values)
            print("Invalid input. Please enter a valid number.")

    # Calculate the average
    if count > 0:
        average = total_sum / count
        print(f"\nThe average of the {count} numbers is: {average:.2f}")
    else:
        print("No numbers were entered to calculate the average.")


# Run the program
if __name__ == "__main__":
    calculate_average()
