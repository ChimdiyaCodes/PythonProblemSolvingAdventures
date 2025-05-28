# Exercise 104: Sorted Order

# Write a program that reads integers from the user and stores them in a list. Your
# program should continue reading values until the user enters 0. Then it should display
# all of the values entered by the user (except for the 0) in order from smallest to largest,
# with one value appearing on each line. Use either the sort method or the sorted
# function to sort the list.

# solution

numbers = []

print("\nEnter integers one by one. Enter 0 to exit.")

while True:
    try:
        user_input = int(input("\nEnter a number: "))

        if user_input == 0:
            break
        numbers.append(user_input)

    except ValueError:
        print("Invalid input. Please enter an integer.")

# sort the numbers
numbers.sort()

# display the sorted numbers
print("\nSorted numbers in ascending order:")
for number in numbers:
    print(number)
