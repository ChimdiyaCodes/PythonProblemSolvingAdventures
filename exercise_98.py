# Exercise 98: Hexadecimal and Decimal Digits

# Write two functions, hex2int and int2hex, that convert between hexadecimal
# digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F) and base 10 integers. The
# hex2int function is responsible for converting a string containing a single hexadecimal digit to a base 10 integer, while the int2hex function is responsible for converting an integer between 0 and 15 to a single hexadecimal digit. Each function
# will take the value to convert as its only parameter and return the converted value
# as the function’s only result. Ensure that the hex2int function works correctly for
# both uppercase and lowercase letters. Your functions should end the program with a
# meaningful error message if an invalid parameter is provided.

# solution

def hex_to_int(hex_digit):
    try:
        if not isinstance(hex_digit, str) or len(hex_digit) != 1:
            raise ValueError("Input must be a single character.")

        hex_digit = hex_digit.upper()
        hex_map = {
            '0': 0, '1': 1, '2': 2, '3': 3,
            '4': 4, '5': 5, '6': 6, '7': 7,
            '8': 8, '9': 9, 'A': 10, 'B': 11,
            'C': 12, 'D': 13, 'E': 14, 'F': 15
        }

        if hex_digit not in hex_map:
            raise ValueError("Invalid hexadecimal digit. Must be 0-9 or A-F.")

        return hex_map[hex_digit]

    except ValueError as e:
        print(f"Error in hex2int: {e}")
        return None


def int_to_hex(number):
    try:
        if not isinstance(number, int):
            raise ValueError("Input must be an integer.")
        if not 0 <= number <= 15:
            raise ValueError("Input must be between 0 and 15.")

        hex_map = "0123456789ABCDEF"
        return hex_map[number]

    except ValueError as e:
        print(f"Error in int2hex: {e}")
        return None


# Interactive Loop for Testing
while True:
    print("\nChoose an option:")
    print("1. Convert Hexadecimal to Integer")
    print("2. Convert Integer to Hexadecimal")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        user_input = input(
            "Enter a single hexadecimal digit (0-9, A-F): ").strip()
        result = hex_to_int(user_input)
        if result is not None:
            print(f"The decimal value of '{user_input}' is {result}.")

    elif choice == "2":
        user_input = input("Enter an integer between 0 and 15: ").strip()
        try:
            num = int(user_input)
            result = int_to_hex(num)
            if result is not None:
                print(f"The hexadecimal digit for {num} is '{result}'.")
        except ValueError:
            print("Error: You must enter a valid integer.")

    elif choice == "3":
        print("Exiting program, goodbye.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
