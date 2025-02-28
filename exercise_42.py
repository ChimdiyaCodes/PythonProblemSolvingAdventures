# Exercise 42: Frequency To Note

# In the previous question you converted from note name to frequency. In this question
# you will write a program that reverses that process. Begin by reading a frequency
# from the user. If the frequency is within one Hertz of a value listed in the table in
# the previous question then report the name of the note. Otherwise report that the
# frequency does not correspond to a known note. In this exercise you only need to
# consider the notes listed in the table. There is no need to consider notes from other
# octaves.

# solution:

def frequency_to_note(frequency):
    # Dictionary to store the frequencies of notes in the 4th octave
    note_frequencies = {
        'C4': 261.63,
        'D4': 293.66,
        'E4': 329.63,
        'F4': 349.23,
        'G4': 392.00,
        'A4': 440.00,
        'B4': 493.88
    }

    # Check if the frequency is within ±1 Hz of any note's frequency
    for note, note_freq in note_frequencies.items():
        if abs(frequency - note_freq) <= 1:
            return note

    # If no match is found, return None
    return None


# Main program
if __name__ == "__main__":
    while True:
        try:
            # Read the frequency from the user
            user_frequency = float(input("\nEnter a frequency (in Hz): "))

            # Validate that the frequency is a positive number
            if user_frequency <= 0:
                print("Frequency must be a positive number. Please try again.")
                continue

            # Convert the frequency to a note
            result = frequency_to_note(user_frequency)

            # Display the result
            if result:
                print(
                    f"\nThe frequency {user_frequency:.2f} Hz corresponds to the note {result}.")
            else:
                print(
                    f"\nThe frequency {user_frequency:.2f} Hz does not correspond to a known note.")

            break  # Exit the loop if the input is valid and processed

        except ValueError:
            print("Invalid input. Please enter a numeric value for the frequency.")
