# Exercise 121: Count the Elements

# Python’s standard library includes a method named count that determines how
# many times a specific value occurs in a list. In this exercise, you will create a new
# function named countRange which determines and returns the number of elements
# within a list that are greater than or equal to some minimum value and less than some
# maximum value. Your function will take three parameters: the list, the minimum
# value and the maximum value. It will return an integer result greater than or equal to
# 0. Include a main program that demonstrates your function for several different lists,
# minimum values and maximum values. Ensure that your program works correctly
# for both lists of integers and lists of floating point numbers.

def countRange(values, minimum, maximum):

    # Counts how many elements in 'values' are >= minimum and < maximum.
    # Returns an integer count.

    count = 0
    for v in values:
        if minimum <= v < maximum:
            count += 1
    return count


def get_list_from_user():
    # Prompts user for a list of numbers and validates input.
    while True:
        try:
            user_input = input("\nEnter numbers separated by spaces: ").strip()
            if not user_input:  # empty input check
                print("You must enter at least one number!")
                continue
            values = [float(x)
                      for x in user_input.split()]  # convert all to float
            return values
        except ValueError:
            print("Invalid input! Please enter only numbers separated by spaces.")


def get_number(prompt):
    # Prompts user for a single number with validation.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    print("\nThis program counts how many numbers in a list fall within a given range.")

    # Get list from user
    values = get_list_from_user()

    # Get min and max
    while True:
        min_val = get_number("\nEnter the minimum value: ")
        max_val = get_number("\nEnter the maximum value: ")

        if min_val >= max_val:
            print("Minimum must be less than maximum! Try again.")
        else:
            break

    # Call function
    result = countRange(values, min_val, max_val)

    # Show result
    print(f"\nList: {values}")
    print(f"Range: [{min_val}, {max_val})")
    print(f"Count of numbers within range: {result}")


# Run the program
if __name__ == "__main__":
    main()
