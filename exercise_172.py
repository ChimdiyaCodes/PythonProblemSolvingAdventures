# Exercise 172: Element Sequences

# Another game that some people play with the names of chemical elements involves
# constructing a sequence of elements where each element in the sequence begins with
# the last letter of its predecessor. For example, if a sequence begins with Hydrogen,
# then the next element must be an element that begins with N, such as Nickel. The
# element following Nickel must begin with L, such as Lithium. The element sequence
# that is constructed can not contain any duplicates.
# Write a program that reads the name of an element from the user. Your program
# should use a recursive function to find the longest sequence of elements that begins
# with the entered element. Then it should display the sequence. Ensure that your
# program responds in a reasonable way if the user does not enter a valid element name.
# Hint: It may take your program up to two minutes to find the longest sequence
# for some elements. As a result, you might want to use elements like Molybdenum and Magnesium as your first test cases. Each has a longest sequence
# that is only 8 elements long which your program should find in a fraction of a
# second.

# solution:

# --------------------------
#   ELEMENT SEQUENCE GAME
# --------------------------

# List of all 118 chemical elements
# --------------------------
#   ELEMENT SEQUENCE GAME
# --------------------------

# List of all 118 chemical elements
ELEMENTS = [
    "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen",
    "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminium", "Silicon", "Phosphorus",
    "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium",
    "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
    "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium",
    "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium",
    "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin",
    "Antimony", "Tellurium", "Iodine", "Xenon", "Caesium", "Barium", "Lanthanum",
    "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium",
    "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium",
    "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium",
    "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium",
    "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium",
    "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium",
    "Californium", "Einsteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium",
    "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium",
    "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium",
    "Moscovium", "Livermorium", "Tennessine", "Oganesson"
]


def find_longest_chain(current, remaining):
    """
    Recursively finds the longest chain starting from `current`.
    """
    last_letter = current[-1].lower()

    # Find elements that start with the last letter of current
    candidates = [
        elem for elem in remaining
        if elem.lower().startswith(last_letter)
    ]

    if not candidates:
        return [current]  # No extension possible

    best_chain = [current]

    for next_elem in candidates:
        new_remaining = remaining.copy()
        new_remaining.remove(next_elem)

        next_chain = find_longest_chain(next_elem, new_remaining)

        if len(next_chain) + 1 > len(best_chain):
            best_chain = [current] + next_chain

    return best_chain


def main():
    user_input = input("Enter the name of a chemical element: ").strip()

    # Validate element
    if user_input.capitalize() not in ELEMENTS:
        print("Invalid element name. Please enter a valid chemical element.")
        return

    start = user_input.capitalize()
    remaining = ELEMENTS.copy()
    remaining.remove(start)

    print("\nSearching for the longest sequence... (This may take a while)\n")

    longest_sequence = find_longest_chain(start, remaining)

    print("Longest sequence found:")
    for elem in longest_sequence:
        print(elem)


# Run the program
if __name__ == "__main__":
    main()
