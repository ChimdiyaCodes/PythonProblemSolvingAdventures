# Exercise 120: Is a List already in Sorted Order?

# Write a function that determines whether or not a list of values is in sorted order
# (either ascending or descending). The function should return True if the list is
# already sorted. Otherwise it should return False. Write a main program that reads
# a list of numbers from the user and then uses your function to report whether or not
# the list is sorted.
# Make sure you consider these questions when completing this exercise: Is a
# list that is empty in sorted order? What about a list containing one element?

def is_sorted(values):

    if len(values) <= 1:
        return "The list is trivially sorted (ascending and descending)"

    ascending = all(values[i] <= values[i + 1] for i in range(len(values) - 1))
    descending = all(values[i] >= values[i + 1]
                     for i in range(len(values) - 1))

    if ascending:
        return "The list is sorted in ascending order."
    elif descending:
        return "The list is sorted in descending order."
    else:
        return "The list is not sorted."


def main():
    print("Welcome! 👋")
    print("This program lets you enter numbers and tells you if they are sorted in ascending or descending order.")
    print("If they are not sorted, it will say so.\n")
    while True:
        try:
            # Prompt user input
            user_input = input("\nEnter numbers separated by spaces: ").strip()

            if not user_input:  # If empty string entered
                print("You must enter at least one number. Please try again.")
                continue

            # Convert input to a list of floats (to handle decimals too)
            numbers = [float(x) for x in user_input.split()]

            # Call function
            result = is_sorted(numbers)
            print(result)

            break  # Exit loop after successful check

        except ValueError:
            print("Invalid input! Please enter only numbers separated by spaces.")


if __name__ == "__main__":
    main()
