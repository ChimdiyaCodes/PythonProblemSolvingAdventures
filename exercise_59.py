# Exercise 59: Is a License Plate Valid?

# In a particular jurisdiction, older license plates consist of three uppercase letters
# followed by three numbers. When all of the license plates following that pattern had
# been used, the format was changed to four numbers followed by three uppercase
# letters.
# Write a program that begins by reading a string of characters from the user. Then
# your program should display a message indicating whether the characters are valid
# for an older style license plate or a newer style license plate. Your program should
# display an appropriate message if the string entered by the user is not valid for either
# style of license plate.

# solution:

def is_older_style(plate):
    """
    Check if the license plate follows the older style format: 3 letters + 3 numbers.
    """
    return (
        len(plate) == 6
        and plate[:3].isalpha()
        and plate[:3].isupper()
        and plate[3:].isdigit()
    )


def is_newer_style(plate):
    """
    Check if the license plate follows the newer style format: 4 numbers + 3 letters.
    """
    return (
        len(plate) == 7
        and plate[:4].isdigit()
        and plate[4:].isalpha()
        and plate[4:].isupper()
    )


def validate_license_plate():
    """
    Validate the license plate input and determine its style.
    """
    while True:
        try:
            # Prompt the user for input
            plate = input("\nEnter a license plate: ").strip()

            # Validate the input
            if is_older_style(plate):
                print("\nValid older style license plate.")
                break
            elif is_newer_style(plate):
                print("\nValid newer style license plate.")
                break
            else:
                print("\nInvalid license plate. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


# Run the program
if __name__ == "__main__":
    validate_license_plate()
