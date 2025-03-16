# Exercise 67: Admission Price

# A particular zoo determines the price of admission based on the age of the guest.
# Guests 2 years of age and less are admitted without charge. Children between 3 and
# 12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission
# for all other guests is $23.00.
# Create a program that begins by reading the ages of all of the guests in a group
# from the user, with one age entered on each line. The user will enter a blank line to
# indicate that there are no more guests in the group. Then your program should display
# the admission cost for the group with an appropriate message. The cost should be
# displayed using two decimal places.

# solution:

def get_age(prompt):
    while True:
        age_input = input(prompt).strip()
        if age_input == "":
            return None  # Blank line indicates no more guests
        try:
            age = int(age_input)
            if age < 0:
                print("Age cannot be negative. Please enter a valid age.")
            else:
                return age
        except ValueError:
            print("Invalid input. Please enter a valid integer for age.")


def calculate_admission_cost(age):
    if age <= 2:
        return 0.00  # Free for guests 2 years or younger
    elif 3 <= age <= 12:
        return 14.00  # Child admission
    elif age >= 65:
        return 18.00  # Senior admission
    else:
        return 23.00  # Standard admission


def main():
    total_cost = 0.0

    print("\nEnter the ages of the guests (one per line). Enter a blank line to finish:")
    while True:
        age = get_age("Age: ")
        if age is None:
            break  # Exit loop if user enters a blank line
        total_cost += calculate_admission_cost(age)

    print(f"The total admission cost for the group is: ${total_cost:.2f}")


if __name__ == "__main__":
    main()
