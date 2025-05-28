# Exercise 106: Remove Outliers

# When analysing data collected as part of a science experiment it may be desirable
# to remove the most extreme values before performing other calculations. Write a
# function that takes a list of values and an non-negative integer, n, as its parameters.
# The function should create a new copy of the list with the n largest elements and the
# n smallest elements removed. Then it should return the new copy of the list as the
# function’s only result. The order of the elements in the returned list does not have to
# match the order of the elements in the original list.
# Write a main program that demonstrates your function. Your function should read
# a list of numbers from the user and remove the two largest and two smallest values
# from it. Display the list with the outliers removed, followed by the original list. Your
# program should generate an appropriate error message if the user enters less than 4
# values.

# solution

def remove_outliers(data, n):
    # Removes the n smallest and n largest elements from the list and returns a new list.
    if len(data) < 2 * n:
        raise ValueError(
            f"List must have at least {2 * n} elements to remove outliers.")

    sorted_data = sorted(data)
    return sorted_data[n: -n]  # Remove n smallest and n largest


def get_user_input():
    # Collects numbers from the user with input validation.
    # Keeps asking until at least 4 numbers are provided.
    while True:
        numbers = []
        print("\nEnter at least 4 numbers (press Enter without input when you're done):")

        while True:
            user_input = input("Enter a number: ")
            if user_input == "":
                break
            try:
                number = float(user_input)
                numbers.append(number)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if len(numbers) < 4:
            print("❌ You entered less than 4 numbers. Please try again.\n")
        else:
            return numbers


def main():
    numbers = get_user_input()

    try:
        cleaned_data = remove_outliers(numbers, 2)
        print(
            f"\n✅ Your list of numbers with outliers removed: {cleaned_data}")
        print(f"📦 Your original list: {numbers}")
    except ValueError as e:
        print(f"Error: {e}")


# Run the program
main()
