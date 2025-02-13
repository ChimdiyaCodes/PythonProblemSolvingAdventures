# Exercise 3: Area of a room

# Write a program that asks the user to enter the width and length of a room. Once
# the values have been read, your program should compute and display the area of the
# room. The length and the width will be entered as floating point numbers. Include
# units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with.

# Solution:

# Prompt the user for input
width = float(input("Enter the width of the room in meters: "))
length = float(input("\nEnter the length of the room in meters: "))

# Display the entered values
print(f"\nWidth: {width}m")
print(f"\nLength: {length}m")

# Calculate and display the area
area = width * length
print(f"\nTotal area: {area:.2f} m²")  # Formats area to 2 decimal places
