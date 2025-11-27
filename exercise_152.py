# Exercise 152:What’s that Element Again?

# Write a program that reads a file containing information about chemical elements
# and stores it in one or more appropriate data structures. Then your program should
# read and process input from the user. If the user enters an integer then your program
# should display the symbol and name of the element with the number of protons
# entered. If the user enters a string then your program should display the number
# of protons for the element with that name or symbol. Your program should display
# an appropriate error message if no element exists for the name, symbol or number of protons entered. Continue to read input from the user until a blank line is
# entered.

# solution

def load_elements(filename):
    """
    Reads a file and stores element data into dictionaries for fast lookup.
    """
    proton_to_element = {}
    name_to_proton = {}
    symbol_to_proton = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.split()

                if len(parts) < 3:
                    continue  # skip lines that are not valid

                proton = int(parts[0])       # number of protons (key)
                name = parts[1]             # element name
                symbol = parts[2]           # element symbol

                # Store in dictionaries
                proton_to_element[proton] = (name, symbol)
                name_to_proton[name.lower()] = proton
                symbol_to_proton[symbol.lower()] = proton

        return proton_to_element, name_to_proton, symbol_to_proton

    except FileNotFoundError:
        print("❌ Error: The file was not found. Check the filename.")
        return None, None, None


def element_lookup(proton_to_element, name_to_proton, symbol_to_proton):
    """
    Takes user input and finds the matching element by proton number, name, or symbol.
    """
    while True:
        user_input = input(
            "\nEnter a proton number, element name, symbol (or blank to exit): ").strip()

        if user_input == "":
            print("Program ended. Goodbye! 👋")
            break  # Exit the loop

        # 1️⃣ Try numeric input (proton number)
        try:
            proton_number = int(user_input)
            if proton_number in proton_to_element:
                name, symbol = proton_to_element[proton_number]
                print(f"👉 {proton_number} protons = {name} ({symbol})")
            else:
                print("❌ No element found with that number of protons.")
            continue  # skip string handling

        except ValueError:
            pass  # Not a number → move on to string checks

        # 2️⃣ Try name or symbol input
        user_input_lower = user_input.lower()

        if user_input_lower in name_to_proton:
            print(
                f"👉 {user_input} = {name_to_proton[user_input_lower]} protons")
        elif user_input_lower in symbol_to_proton:
            print(
                f"👉 {user_input} = {symbol_to_proton[user_input_lower]} protons")
        else:
            print("❌ Invalid input. No such element found.")


# ---- MAIN PROGRAM ----
filename = "elements.txt"  # change this if needed

proton_to_element, name_to_proton, symbol_to_proton = load_elements(filename)

if proton_to_element:   # Proceed only if data was loaded correctly
    element_lookup(proton_to_element, name_to_proton, symbol_to_proton)
