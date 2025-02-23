# Exercise 31: Sum of the Digits in an Integer

# Develop a program that reads a four-digit integer from the user and displays the sum
# of the digits in the number. For example, if the user enters 3141 then your program
# should display 3+1+4+1=9.

# Solution:

while True:
    try:
        # Prompt the user to enter a four-digit integer

        number = int(input("\nEnter a four-digit integer: "))

        # Validate that the number is a four-digit integer

        if 1000 <= number <= 9999:
            # Extract each digit

            thousands = number // 1000          # Extract the thousands place
            hundreds = (number % 1000) // 100   # Extract the hundreds place
            tens = (number % 100) // 10        # Extract the tens place
            units = number % 10                 # Extract the units place

            # Calculate the sum of the digits

            digit_sum = thousands + hundreds + tens + units

            # Display the result

            print(
                f"\nThe sum of the digits is: {thousands} + {hundreds} + {tens} + {units} = {digit_sum}")
            break  # Exit the loop after successful execution
        else:
            print(
                "Invalid input! Please enter a valid four-digit integer (between 1000 and 9999).")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
