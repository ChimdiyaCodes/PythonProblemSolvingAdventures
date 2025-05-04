# Exercise 91: Operator Precedence

# Write a function named precedence that returns an integer representing the precedence of a mathematical operator. A string containing the operator will be passed to
# the function as its only parameter. Your function should return 1 for + and -, 2 for *
# and /, and 3 for ˆ. If the string passed to the function is not one of these operators
# then the function should return -1. Include a main program that reads an operator
# from the user and either displays the operator’s precedence or an error message indicating that the input was not an operator. Your main program should only run when
# the file containing your solution has not been imported into another program.

# solution:

def precedence(op):
    """
    Returns the precedence level of a mathematical operator.
    + or - -> 1
    * or / -> 2
    ^      -> 3
    Other  -> -1
    """
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    else:
        return -1


def main():
    print("\nOperator Precedence Checker")
    print("Supported operators: +  -  *  /  ^")
    print("Enter 'q' to quit.\n")

    while True:
        try:
            user_input = input("\nEnter a mathematical operator: ").strip()

            if user_input.lower() == 'q':
                print("Exiting the program, goodbye.")
                break

            # Input must be exactly one character long
            if len(user_input) != 1:
                print("\nError: Please enter a single character.")
                continue

            result = precedence(user_input)

            if result == -1:
                print("\nError: That is not a valid operator.\n")
            else:
                print(f"\nThe precedence of '{user_input}' is {result}.\n")

        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")


# This ensures the main program only runs when the file is executed directly
if __name__ == "__main__":
    main()
