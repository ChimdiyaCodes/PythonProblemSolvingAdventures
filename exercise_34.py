# Exercise 34: Even or Odd?

# Write a program that reads an integer from the user. Then your program should
# display a message indicating whether the integer is even or odd.

# Solution

while True:
    try:
        # take user input

        number = int(input("\nEnter an integer: "))

        # check remainder using modulo operator

        remainder = number % 2

        # display result

        if remainder == 0:
            print(f"\nThe number {number} is an even number.")
            break
        else:
            print(f"\nThe number {number} is an odd number.")
            break
    except ValueError:
        print("Please enter a valid integer.")
