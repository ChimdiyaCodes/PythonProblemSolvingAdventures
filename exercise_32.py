# Exercise 32: Sort 3 Integers

# Create a program that reads three integers from the user and displays them in sorted
# order (from smallest to largest). Use the min and max functions to find the smallest
# and largest values. The middle value can be found by computing the sum of all three
# values, and then subtracting the minimum value and the maximum value.

# Solution

print("\nWelcome! This program sorts three integers in ascending order.")
print("You will be prompted to enter three integers (a, b, and c).\n")


def correct_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():  # take 3 integers
    a = correct_integer("a = ")
    b = correct_integer("b = ")
    c = correct_integer("c = ")

    # smallest integer

    smallest = min(a, b, c)

    # largest integer

    largest = max(a, b, c)

    # middle integer

    middle = (a + b + c) - smallest - largest

    # display result in ascending order

    print(
        f"\nYour numbers in ascending order: {smallest}, {middle}, {largest}")


if __name__ == "__main__":
    main()
