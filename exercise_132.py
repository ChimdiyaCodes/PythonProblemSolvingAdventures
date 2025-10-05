# Exercise 132: Postal Codes

# In a Canadian postal code, the first, third and fifth characters are letters while the
# second, fourth and sixth characters are numbers. The province can be determined
# from the first character of a postal code, as shown in the following table. No valid
# postal codes currently begin with D, F, I, O, Q, U, W, or Z.
# Province First character(s)
# Newfoundland A
# Nova Scotia B
# Prince Edward Island C
# New Brunswick E
# Quebec G, H and J
# Ontario K, L, M, N and P
# Manitoba R
# Saskatchewan S
# Alberta T
# British Columbia V
# Nunavut X
# Northwest Territories X
# Yukon Y
# The second character in a postal code identifies whether the address is rural or
# urban. If that character is a 0 then the address is rural. Otherwise it is urban.
# Create a program that reads a postal code from the user and displays the province
# associated with it, along with whether the address is urban or rural. For example,
# if the user enters T2N 1N4 then your program should indicate that the postal code
# is for an urban address in Alberta. If the user enters X0A 1B2 then your program
# should indicate that the postal code is for a rural address in Nunavut or Northwest
# Territories. Use a dictionary to map from the first character of the postal code to the
# province name. Display a meaningful error message if the postal code begins with
# an invalid character.

# solution:

def get_postal_info():
    provinces = {
        "A": "Newfoundland",
        "B": "Nova Scotia",
        "C": "Prince Edward Island",
        "E": "New Brunswick",
        "G": "Quebec", "H": "Quebec", "J": "Quebec",
        "K": "Ontario", "L": "Ontario", "M": "Ontario", "N": "Ontario", "P": "Ontario",
        "R": "Manitoba",
        "S": "Saskatchewan",
        "T": "Alberta",
        "V": "British Columbia",
        "X": "Nunavut or Northwest Territories",
        "Y": "Yukon"
    }

    invalid_start = {"D", "F", "I", "O", "Q", "U", "W", "Z"}

    while True:
        try:
            postal_code = input(
                "\nEnter a Canadian postal code (e.g., T2N1N4): ").strip().upper()
            # Remove space if included
            postal_code = postal_code.replace(" ", "")

            # Check length
            if len(postal_code) != 6:
                raise ValueError(
                    "Postal code must have 6 characters (letters and digits).")

            # Check format: LNLNLN
            for i in range(6):
                if i % 2 == 0:  # Even positions (0,2,4) must be letters
                    if not postal_code[i].isalpha():
                        raise ValueError(f"Character {i+1} must be a LETTER.")
                else:  # Odd positions (1,3,5) must be digits
                    if not postal_code[i].isdigit():
                        raise ValueError(f"Character {i+1} must be a DIGIT.")

            # Get province
            first_char = postal_code[0]
            if first_char in invalid_start or first_char not in provinces:
                raise ValueError(
                    f"No valid province starts with '{first_char}'.")

            province = provinces[first_char]

            # Get rural/urban
            if postal_code[1] == "0":
                address_type = "Rural"
            else:
                address_type = "Urban"

            print(
                f"The postal code {postal_code} is for a {address_type} address in {province}.")
            break  # Exit loop when successful

        except ValueError as ve:
            print(f"Error: {ve}. Please try again.")
        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.")
