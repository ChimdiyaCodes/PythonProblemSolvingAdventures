# Exercise 54:Wavelengths of Visible Light

# The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
# spectrum is continuous, it is often divided into 6 colors as shown below:

# Color Wavelength (nm)
# Violet 380 to less than 450
# Blue 450 to less than 495
# Green 495 to less than 570
# Yellow 570 to less than 590
# Orange 590 to less than 620
# Red 620 to 750
# Write a program that reads a wavelength from the user and reports its color. Display
# an appropriate error message if the wavelength entered by the user is outside of the
# visible spectrum.

# solution:

def determine_light_color():
    while True:
        try:
            # Prompt the user for the wavelength
            wavelength = float(
                input("\nEnter the wavelength of visible light (in nm): "))

            # Check if the wavelength is within the visible spectrum
            if 380 <= wavelength < 450:
                color = "Violet"
            elif 450 <= wavelength < 495:
                color = "Blue"
            elif 495 <= wavelength < 570:
                color = "Green"
            elif 570 <= wavelength < 590:
                color = "Yellow"
            elif 590 <= wavelength < 620:
                color = "Orange"
            elif 620 <= wavelength <= 750:
                color = "Red"
            else:
                # If the wavelength is outside the visible spectrum, raise an error
                raise ValueError(
                    "Wavelength is outside the visible spectrum (380–750 nm).")

            # Display the color
            print(f"\nThe color corresponding to {wavelength} nm is {color}.")
            break  # Exit the loop if the input is valid

        except ValueError as e:
            # Handle invalid inputs (non-numeric or out-of-range values)
            print(
                f"Error: {e}. Please enter a valid wavelength between 380 and 750 nm.")


# Run the program
determine_light_color()
