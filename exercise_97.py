# Exercise 97: Random Good Password

# Using your solutions to Exercises 94 and 96, write a program that generates a random
# good password and displays it. Count and display the number of attempts that were
# needed before a good password was generated. Structure your solution so that it
# imports the functions you wrote previously and then calls them from a function
# named main in the file that you create for this exercise.

# solution

from exercise_94 import generate_password
from exercise_96 import good_password


def main():
    attempts = 0
    final_good_password = None

    while True:
        password = generate_password()
        attempts += 1
        if good_password(password):
            final_good_password = password
            break
    print("\n----This program makes attempts to generate a random good password for you and tells you the number of attempts----")
    print(f"\n🔐 Good password generated: {final_good_password}")
    print(f"🔁 Number of attempts: {attempts}")


# Make sure this only runs when the file is executed directly
if __name__ == "__main__":
    main()
