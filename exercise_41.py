# Exercise 41: Note To Frequency

# The following table lists an octave of music notes, beginning with middle C, along
# with their frequencies.
# Note Frequency (Hz)
# C4 261.63
# D4 293.66
# E4 329.63
# F4 349.23
# G4 392.00
# A4 440.00
# B4 493.88
# Begin by writing a program that reads the name of a note from the user and
# displays the note’s frequency. Your program should support all of the notes listed
# previously.
# Once you have your program working correctly for the notes listed previously you
# should add support for all of the notes from C0 to C8. While this could be done by
# adding many additional cases to your if statement, such a solution is cumbersome,
# inelegant and unacceptable for the purposes of this exercise. Instead, you should
# exploit the relationship between notes in adjacent octaves. In particular, the frequency
# of any note in octave n is half the frequency of the corresponding note in octave n+1.
# By using this relationship, you should be able to add support for the additional notes
# without adding additional cases to your if statement.
# Hint: To complete this exercise you will need to extract individual characters
# from the two-character note name so that you can work with the letter and
# the octave number separately. Once you have separated the parts, compute the
# frequency of the note in the fourth octave using the data in the table above.
# Then divide the frequency by 24−x , where x is the octave number entered by
# the user. This will halve or double the frequency the correct number of times.

# solution:
def note_to_frequency(note):
    # Dictionary to store the base frequencies of notes in the 4th octave
    base_frequencies = {
        'C': 261.63,
        'D': 293.66,
        'E': 329.63,
        'F': 349.23,
        'G': 392.00,
        'A': 440.00,
        'B': 493.88
    }

    # Extract the note letter and octave number from the input
    note_letter = note[0].upper()  # Ensure the note letter is uppercase
    # Extract the octave number (can be multi-digit, e.g., "10")
    octave = note[1:]

    # Validate the note letter
    if note_letter not in base_frequencies:
        return "Invalid note letter. Please enter a valid note (C, D, E, F, G, A, B)."

    # Validate the octave number
    try:
        octave = int(octave)
        if octave < 0 or octave > 8:
            return "Invalid octave number. Please enter an octave between 0 and 8."
    except ValueError:
        return "Invalid octave format. Please enter a valid number for the octave."

    # Get the base frequency of the note in the 4th octave
    base_frequency = base_frequencies[note_letter]

    # Calculate the frequency of the note in the desired octave
    frequency = base_frequency / (2 ** (4 - octave))

    return frequency


# Main program
if __name__ == "__main__":
    while True:
        # Read the note from the user
        user_note = input(
            "\nEnter a musical note (e.g., C4, D5, etc.): ").strip()

        # Validate the input format (must be at least 2 characters: note + octave)
        if len(user_note) < 2 or not user_note[0].isalpha() or not user_note[1:].isdigit():
            print(
                "Invalid input format. Please enter a note in the format 'C4', 'D5', etc.")
            continue

        # Calculate and display the frequency
        result = note_to_frequency(user_note)
        if isinstance(result, float):
            print(f"\nThe frequency of {user_note} is {result:.2f} Hz.")
            break  # Exit the loop if the result is valid
        else:
            print(result)  # Display error message and prompt again
