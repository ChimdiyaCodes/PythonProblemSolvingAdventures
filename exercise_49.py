# Exercise 49: Richter Scale

# The following table contains earthquake magnitude ranges on the Richter scale and
# their descriptors:
# Magnitude Descriptor
# Less than 2.0 Micro
# 2.0 to less than 3.0 Very minor
# 3.0 to less than 4.0 Minor
# 4.0 to less than 5.0 Light
# 5.0 to less than 6.0 Moderate
# 6.0 to less than 7.0 Strong
# 7.0 to less than 8.0 Major
# 8.0 to less than 10.0 Great
# 10.0 or more Meteoric
# Write a program that reads a magnitude from the user and displays the appropriate
# descriptor as part of a meaningful message. For example, if the user enters 5.5 then
# your program should indicate that a magnitude 5.5 earthquake is considered to be a
# moderate earthquake.

# solution:

def get_ritcher_descriptor(magnitude):
    # determine the descriptor based on the magnitude
    if magnitude < 2.0:
        return "Micro"
    elif 2.0 <= magnitude < 3.0:
        return "Minor"
    elif 4.0 <= magnitude < 5.0:
        return "Light"
    elif 5.0 <= magnitude < 6.0:
        return "Moderate"
    elif 6.0 <= magnitude < 7.0:
        return "Strong"
    elif 7.0 <= magnitude < 8.0:
        return "Major"
    elif 8.0 <= magnitude < 10.0:
        return "Great"
    else:
        return "Meteoric"


def main():
    while True:
        try:
            # prompt the user for a magnitude
            magnitude = float(input("\nEnter the earthquake magnitude: "))

            # validate that the magnitude is non-negative
            if magnitude < 0:
                print("Please enter a non-negative number.")
                continue

            descriptor = get_ritcher_descriptor(magnitude)

            # display the result
            print(
                f"\nAn earthquake of {magnitude} magnitude is considered to be a {descriptor.lower()} earthquake.")
            break

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
