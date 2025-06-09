# Exercise 112: Below and Above Average

# Write a program that reads numbers from the user until a blank line is entered. Your
# program should display the average of all of the values entered by the user. Then
# the program should display all of the below average values, followed by all of the
# average values (if any), followed by all of the above average values. An appropriate
# label should be displayed before each list of values.

# solution:

def main():
    print("Enter numbers one by one. Press Enter on a blank line to finish.\n")

    numbers = []

    while True:
        user_input = input("Enter a number (or press Enter to finish): ")

        if user_input == "":
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if len(numbers) == 0:
        print("No numbers were entered.")
        return

    average = sum(numbers) / len(numbers)

    # Categorize numbers
    below_average = []
    equal_to_average = []
    above_average = []

    for num in numbers:
        if num < average:
            below_average.append(num)
        elif num == average:
            equal_to_average.append(num)
        else:
            above_average.append(num)

    # Display results
    print(f"\nAverage of entered numbers: {average:.2f}\n")

    print("Below average values:")
    print(below_average if below_average else "None")

    print("\nEqual to average values:")
    print(equal_to_average if equal_to_average else "None")

    print("\nAbove average values:")
    print(above_average if above_average else "None")


# Run the program
if __name__ == "__main__":
    main()
