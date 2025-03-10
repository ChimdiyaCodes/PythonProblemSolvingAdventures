# Exercise 55: Frequency to Name

# Electromagnetic radiation can be classified into one of 7 categories according to its
# frequency, as shown in the table below:
# Name Frequency range (Hz)
# Radio waves Less than 3 × 109
# Microwaves 3 × 109 to less than 3 × 1012
# Infrared light 3 × 1012 to less than 4.3 × 1014
# Visible light 4.3 × 1014 to less than 7.5 × 1014
# Ultraviolet light 7.5 × 1014 to less than 3 × 1017
# X-rays 3 × 1017 to less than 3 × 1019
# Gamma rays 3 × 1019 or more
# Write a program that reads the frequency of the radiation from the user and displays
# the appropriate name.

# solution:

def classify_radiation():
    while True:
        try:
            # Prompt the user for the frequency
            frequency = float(
                input("\nEnter the frequency of the radiation (in Hz): "))

            # Check if the frequency is valid (non-negative)
            if frequency < 0:
                raise ValueError("Frequency cannot be negative.")

            # Determine the category based on the frequency
            if frequency < 3e9:
                category = "Radio waves"
            elif 3e9 <= frequency < 3e12:
                category = "Microwaves"
            elif 3e12 <= frequency < 4.3e14:
                category = "Infrared light"
            elif 4.3e14 <= frequency < 7.5e14:
                category = "Visible light"
            elif 7.5e14 <= frequency < 3e17:
                category = "Ultraviolet light"
            elif 3e17 <= frequency < 3e19:
                category = "X-rays"
            else:
                category = "Gamma rays"

            # Display the category
            print(
                f"\nThe radiation with a frequency of {frequency} Hz is classified as {category}.")
            break  # Exit the loop if the input is valid

        except ValueError as e:
            # Handle invalid inputs (non-numeric or negative values)
            print(f"Error: {e}. Please enter a valid non-negative frequency.")


# Run the program
classify_radiation()
