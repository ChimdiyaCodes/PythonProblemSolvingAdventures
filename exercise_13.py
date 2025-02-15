# Exercise 13: Making Change

# Consider the software that runs on a self-checkout machine. One task that it must be
# able to perform is to determine how much change to provide when the shopper pays
# for a purchase with cash.
# Write a program that begins by reading a number of cents from the user as an
# integer. Then your program should compute and display the denominations of the
# coins that should be used to give that amount of change to the shopper. The change
# should be given using as few coins as possible. Assume that the machine is loaded
# with pennies, nickels, dimes, quarters, loonies and toonies.

# Solution:

# Function to calculate the change

def make_change(total_cents):
    # Define coin denominations and their names
    denominations = [
        (200, "Toonie"),
        (100, "Loonie"),
        (25, "Quarter"),
        (10, "Dime"),
        (5, "Nickel"),
        (1, "Penny")
    ]

    if total_cents == 0:
        return print("No change needed.")

    # Calculate and display change
    for value, name in denominations:
        count = total_cents // value
        if count > 0:
            print(f"\n{name}{'s' if count > 1 else ''}: {count}")
            total_cents %= value

# Main program


def change():
    while True:
        # Ask the user for the number of cents
        try:
            total_cents = int(input("\nEnter the number of cents: "))
            if total_cents < 0:
                print("Error: Please enter a non-negative number of cents.")
                continue
            else:
                make_change(total_cents)

        # Ask if the user wants to calculate again
            while True:
                calculate_again = input(
                    """\nWould you like to make another change calculation? : 
                    \nEnter \n\nY for YES \n\nN for NO: """)
                if calculate_again.upper() in ['Y', 'YES']:
                    break  # Break the inner loop to do another calculation
                elif calculate_again.upper() in ['N', 'NO']:
                    print("\nThank you for using the change calculator!")
                    return  # Exit the function (and program)
                else:
                    print("\nInvalid input! Please enter Y for yes or N for no.")
                    continue  # Keep asking for valid input

        except ValueError:
            print("Error: Please enter a valid integer.")
            continue


# Run the program
if __name__ == "__main__":
    change()
