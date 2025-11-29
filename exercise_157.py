# Exercise 157: Distinct Names

# In this exercise, you will create a program that reads every file in the baby names data
# set described in Exercise 154. As your program reads the files, it should keep track
# of each name used for a boy and each name used for a girl. Your program should  output two lists. One list will contain all of the names that have been used for girls.
# The other list will contain all of the names that have been used for boys. Neither of
# your lists should contain any repeated values.

# solution

import os  # Allows us to work with folders and files

# Folder that contains all the baby name files
folder = "babynames"

# Sets to store unique names (no duplicates allowed)
boy_names = set()
girl_names = set()

# Loop through ALL files in the folder
for filename in os.listdir(folder):

    # Full path to the file (foldername + filename)
    filepath = os.path.join(folder, filename)

    # Check if it is a boy file
    if filename.startswith("boy"):
        with open(filepath, "r") as file:
            for line in file:
                # Example line: Noah, 20 → we want only "Noah"
                name = line.split(",")[0].strip()
                boy_names.add(name)  # Add to set → set removes duplicates

    # Check if it is a girl file
    elif filename.startswith("girl"):
        with open(filepath, "r") as file:
            for line in file:
                name = line.split(",")[0].strip()
                girl_names.add(name)

# FINAL OUTPUT — sort them for easier reading
print("\n=== ALL DISTINCT BOY NAMES ===")
print(sorted(boy_names))

print("\n=== ALL DISTINCT GIRL NAMES ===")
print(sorted(girl_names))
