# Exercise 108: Negatives, Zeros and Positives

# Create a program that reads integers from the user until a blank line is entered. Once
# all of the integers have been read your program should display all of the negative
# numbers, followed by all of the zeros, followed by all of the positive numbers. Within
# each group the numbers should be displayed in the same order that they were entered
#  by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then
# your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program
# should display each value on its own line.

# solution:

# Create three lists for categorizing numbers

negatives = []
zeros = []
positives = []

print("\nEnter integers one by one. Press enter withput typing anything when you're done.")

while True:
    user_input = input("\nEnter an integer: ")

    if user_input == "":
        break  # blank input ends the loop

    try:
        number = int(user_input)

        if number < 0:
            negatives.append(number)
        elif number == 0:
            zeros.append(number)
        else:
            positives.append(number)

    except ValueError:
        # Handle invalid (non-integer) input
        print("Invalid input. Please enter a valid integer or press Enter to finish.")

    # output the results

print("\nNegatives, Zeros, and Positives in order:")

for num in negatives:
    print(num)

for num in zeros:
    print(num)

for num in positives:
    print(num)
