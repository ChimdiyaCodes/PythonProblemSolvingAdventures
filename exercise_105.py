# Exercise 105: Reverse Order

# Write a program that reads integers from the user and stores them in a list. Use 0 as
# a sentinel value to mark the end of the input. Once all of the values have been read
# your program should display them (except for the 0) in reverse order, with one value
# appearing on each line.

# solution

numbers = []

print("\nEnter integers one by one. Enter 0 to finish:")

while True:
    try:
        user_input = int(input("\nEnter a number: "))

        if user_input == 0:
            break  # Sentinel value to stop input
        numbers.append(user_input)

    except ValueError:
        print("Invalid input. Please enter an integer.")

# Reverse and print the numbers
print("\nNumbers in reverse order:")
for number in reversed(numbers):  # You can also use numbers[::-1]
    print(number)
