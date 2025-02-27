# Exercise 39: Sound Levels

# The following table lists the sound level in decibels for several common noises.
# Noise Decibel level (dB)
# Jackhammer 130
# Gas lawnmower 106
# Alarm clock 70
# Quiet room 40
# Write a program that reads a sound level in decibels from the user. If the user
# enters a decibel level that matches one of the noises in the table then your program
# should display a message containing only that noise. If the user enters a number
# of decibels between the noises listed then your program should display a message
# indicating which noises the level is between. Ensure that your program also generates
# reasonable output for a value smaller than the quietest noise in the table, and for a
# value larger than the loudest noise in the table.

# Exercise 39: Sound Levels

# Predefined noise levels and their corresponding decibel values
noise_levels = {
    "Jackhammer": 130,
    "Gas lawnmower": 106,
    "Alarm clock": 70,
    "Quiet room": 40
}

# Prompt the user to enter a sound level in decibels
while True:
    try:
        decibels = float(input("\nEnter the sound level in decibels: "))
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value.")
        continue

    # Determine the output based on the input decibel level
    if decibels == noise_levels["Jackhammer"]:
        print("\nThe sound level corresponds to a Jackhammer.")
        break
    elif decibels == noise_levels["Gas lawnmower"]:
        print("\nThe sound level corresponds to a Gas lawnmower.")
        break
    elif decibels == noise_levels["Alarm clock"]:
        print("\nThe sound level corresponds to an Alarm clock.")
        break
    elif decibels == noise_levels["Quiet room"]:
        print("\nThe sound level corresponds to a Quiet room.")
        break
    elif decibels > noise_levels["Jackhammer"]:
        print("\nThe sound level is louder than a Jackhammer.")
        break
    elif noise_levels["Gas lawnmower"] < decibels < noise_levels["Jackhammer"]:
        print("\nThe sound level is between a Gas lawnmower and a Jackhammer.")
        break
    elif noise_levels["Alarm clock"] < decibels < noise_levels["Gas lawnmower"]:
        print("\nThe sound level is between an Alarm clock and a Gas lawnmower.")
        break
    elif noise_levels["Quiet room"] < decibels < noise_levels["Alarm clock"]:
        print("\nThe sound level is between a Quiet room and an Alarm clock.")
        break
    elif decibels < noise_levels["Quiet room"]:
        print("\nThe sound level is quieter than a Quiet room.")
        break
