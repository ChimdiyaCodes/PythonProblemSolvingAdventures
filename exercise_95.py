# Exercise 95: Random License Plate

# In a particular jurisdiction, older license plates consist of three letters followed by
# three numbers. When all of the license plates following that pattern had been used,
# the format was changed to four numbers followed by three letters.
# Write a function that generates a random license plate. Your function should have
# approximately equal odds of generating a sequence of characters for an old license
# plate or a new license plate. Write a main program that calls your function and
# displays the randomly generated license plate.

# solution

import random
import string


def generate_license_plate():
    """
    Generates a random license plate.
    50% chance of old format (LLLNNN) or new format (NNNNLLL).
    Returns:
        str: Randomly generated license plate.
    """
    # Randomly choose between old and new format
    if random.choice([True, False]):
        # Old format: 3 letters + 3 numbers
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        numbers = ''.join(random.choices(string.digits, k=3))
        return letters + numbers
    else:
        # New format: 4 numbers + 3 letters
        numbers = ''.join(random.choices(string.digits, k=4))
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        return numbers + letters


# Main program
if __name__ == "__main__":
    # Generate and display the license plate
    print(f"\nYour Generated License Plate is: {generate_license_plate()}")
