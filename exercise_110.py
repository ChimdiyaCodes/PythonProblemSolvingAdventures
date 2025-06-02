# Exercise 110: Perfect Numbers

# An integer, n, is said to be perfect when the sum of all of the proper divisors of n is
# equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2,
# 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.
# Write a function that determines whether or not a positive integer is perfect. Your
# function will take one parameter. If that parameter is a perfect number then your func
# tion will return true. Otherwise it will return false. In addition, write a main program
# that uses your function to identify and display all of the perfect numbers between 1
# and 10,000. Import your solution to Exercise 109 when completing this task.

# solution:

# Reuse from Exercise 109
def proper_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

# Exercise 110: Check if a number is perfect


def is_perfect(n):
    return sum(proper_divisors(n)) == n

# Input validation


def get_positive_integer(prompt="Enter a positive integer: "):
    while True:
        user_input = input(prompt)

        if user_input.strip() == "":
            print("Input cannot be blank.")
            continue

        try:
            value = int(user_input)
            if value <= 0:
                print("Number must be greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Main program to find perfect numbers between 1 and 10000


def find_perfect_numbers(limit):
    print(f"\nPerfect numbers between 1 and {limit}:")
    for number in range(1, limit + 1):
        if is_perfect(number):
            print(number)

# Optional: Interactive mode for single number check


def interactive_check():
    number = get_positive_integer(
        "\nEnter a number to check if it is perfect: ")
    if is_perfect(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")


#  Only run when script is executed directly
if __name__ == "__main__":
    # Find and print perfect numbers between 1 and 10000
    find_perfect_numbers(10000)

    # Optional: Allow user to check a number interactively
    while True:
        choice = input(
            """\nWould you like to check another number?
        Enter:
        Y for YES
        N for NO
        > """
        ).strip().upper()

        if choice in ['Y', 'YES']:
            interactive_check()
        elif choice in ['N', 'NO']:
            print("\nThank you for using the calculator!")
            break
        else:
            print("Invalid input! Please enter Y or N.")
