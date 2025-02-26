# Exercise 35: Dog Years

# It is commonly said that one human year is equivalent to 7 dog years. However this
# simple conversion fails to recognize that dogs reach adulthood in approximately two
# years. As a result, some people believe that it is better to count each of the first two
# human years as 10.5 dog years, and then count each additional human year as 4 dog
# years.
# Write a program that implements the conversion from human years to dog years
# described in the previous paragraph. Ensure that your program works correctly for
# conversions of less than two human years and for conversions of two or more human
# years. Your program should display an appropriate error message if the user enters
# a negative number

# Function to convert human years to dog years
def human_to_dog_years(human_years):
    if human_years < 0:
        return "Error: Please enter a non-negative number."
    elif human_years < 2:
        # For less than 2 human years, multiply by 10.5
        dog_years = human_years * 10.5
    else:
        # For 2 or more human years, calculate the first two years as 21 dog years
        # and add 4 dog years for each additional year
        dog_years = 2 * 10.5 + (human_years - 2) * 4
    return dog_years

# Main program


def main():
    try:
        # Take input from the user
        human_years = float(input("Enter the number of human years: "))

        # Convert human years to dog years
        result = human_to_dog_years(human_years)

        # Display the result or error message
        if isinstance(result, str):
            print(result)  # Print error message
        else:
            print(f"{human_years} human years is equivalent to {result} dog years.")
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value.")


# Run the program
if __name__ == "__main__":
    main()
