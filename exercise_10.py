# Exercise 10: Arithmetic

# Create a program that reads two integers, a and b, from the user. Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of ab

# Solution:

import math

while True:
    try:
        # Taking input from the user
        a = int(input("\nEnter your 1st number (a): "))
        b = int(input("\nEnter your 2nd number (b): "))

        # The sum of a and b
        sum_of_numbers = a + b
        print(f"\na + b = {sum_of_numbers}")

        # The difference when b is subtracted from a
        subtract = a - b
        print(f"\na - b = {subtract}")

        # The product of a and b
        product = a * b
        print(f"\na * b = {product}")

        # The quotient when a is divided by b
        if b != 0:
            quotient = a / b
            print(f"\na ÷ b = {quotient}")

            # The remainder when a is divided by b
            remainder = a % b
            print(f"\nRemainder of a ÷ b = {remainder}")
        else:
            print("\nCannot divide by zero!")

        # The result of log10 a
        if a > 0:
            log_result = math.log10(a)
            print(f"\nlog10(a) = {log_result}")
        else:
            print("\nCannot calculate log10 of zero or negative number!")

        # The result of a^b (a raised to power b)
        power = a ** b
        print(f"\na^b = {power}")

        # Keep asking for valid input for calculate again
        while True:
            calculate_again = input(
                """\nWould you like to make another calculation? : 
    \nEnter \n\nY for YES \n\nN for No: """)
            if calculate_again in ['Y', 'y', 'YES', 'yes']:
                break  # Break the inner loop to do another calculation
            elif calculate_again in ['N', 'n', 'NO', 'no']:
                print("\nThank you for using the calculator!")
                exit()  # Exit the program
            else:
                print("\nInvalid input! Please enter Y for yes or N for no.")
                continue  # Keep asking for valid input

    except ValueError:
        print("\nPlease enter valid integers!")
        continue
