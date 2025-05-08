# Exercise 94: Random Password

# Write a function that generates a random password. The password should have a
# random length of between 7 and 10 characters. Each character should be randomly
# selected from positions 33 to 126 in the ASCII table. Your function will not take
# any parameters. It will return the randomly generated password as its only result.
# Display the randomly generated password in your file’s main program. Your main
# program should only run when your solution has not been imported into another file.
# Hint: You will probably find the chr function helpful when completing this
# exercise.

# solution:

import random


def generate_password():
    # Step 1: Generate a random length between 7 and 10
    password_length = random.randint(7, 10)

    # Step 2: Generate characters from ASCII range 33 to 126
    password = ''
    for _ in range(password_length):
        password += chr(random.randint(33, 126))

    # Step 3: Return the generated password
    return password


# Main program logic: Only runs if this script is executed directly
if __name__ == "__main__":
    password = generate_password()
    print(f"\n🔐 Your Generated Password is: {password}")
