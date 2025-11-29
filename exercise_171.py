# Exercise 171: Spelling with Element Symbols

# Each chemical element has a standard symbol that is one, two or three letters long.
# One game that some people like to play is to determine whether or not a word can
# be spelled using only element symbols. For example, silicon can be spelled using

# the symbols Si, Li, C, O and N. However, hydrogen can not be spelled with any
# combination of element symbols.
# Write a recursive function that determines whether or not a word can be spelled
# using only element symbols. Your function will take two parameters: the word that
# you are trying to spell and a list of the symbols that can be used. Your function will
# return two results: a Boolean value indicating whether or not a spelling was found,
# and the string of symbols used to achieve the spelling (or an empty string if no spelling
# exists). Your function should ignore capitalization when searching for a spelling.
# Create a program that uses your function to find and display all of the element
# names that can be spelled using only element symbols. Display the names of the elements along with the sequences of symbols. For example, one line of your output
# will be:
# Silver can be spelled as SiLvEr
# Your program will use the elements data set, which can be downloaded from the
# author’s website. This data set includes the names and symbols of all 118 chemical
# elements.

# solution

# -----------------------------------------
# FULL LIST OF ALL 118 ELEMENT SYMBOLS
# -----------------------------------------
ELEMENT_SYMBOLS = [
    'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
    'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
    'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
    'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
    'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
    'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr',
    'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og'
]


# -----------------------------------------
# RECURSIVE SPELLING FUNCTION
# -----------------------------------------
def spell_with_elements(word, symbols):
    """
    Attempt to spell 'word' using the element symbols in 'symbols'.
    Returns (success: bool, result_string: str)
    """

    # Base case: if the word is empty, success
    if word == "":
        return True, ""

    # Try using the first 1, 2, or 3 letters
    for size in (1, 2, 3):
        part = word[:size].capitalize()

        # If part matches a symbol
        if part in symbols:
            # Recursively spell the remaining word
            success, rest = spell_with_elements(word[size:], symbols)
            if success:
                return True, part + rest

    # If all attempts fail
    return False, ""


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------
def main():
    print("=== SPELLING ELEMENT NAMES USING ELEMENT SYMBOLS ===")

    # List of actual element names (118 elements)
    element_names = [
        "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
        "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium",
        "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
        "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",
        "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin",
        "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",
        "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium",
        "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury",
        "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium",
        "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium",
        "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium",
        "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"
    ]

    print("\nChecking which element names can be spelled using element symbols...\n")

    for name in element_names:
        word = name.lower()
        success, symbols = spell_with_elements(word, ELEMENT_SYMBOLS)
        if success:
            print(f"{name} can be spelled as {symbols}")


if __name__ == "__main__":
    main()
