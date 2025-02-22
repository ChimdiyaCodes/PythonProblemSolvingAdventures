# Exercise 27: Body Mass Index
# Write a program that computes the body mass index (BMI) of an individual. Your
# program should begin by reading a height and weight from the user. Then it should use one of the following two formulas to compute the BMI before displaying it. If
# you read the height in inches and the weight in pounds then body mass index is
# computed using the following formula:
# BMI = weight
# height × height × 703.
# If you read the height in meters and the weight in kilograms then body mass index
# is computed using this slightly simpler formula:
# BMI = weight
# height × height

# Solution:
while True:
    # ask the user for the units

    unit = input("""
    \nYou will be asked to enter your weight and height for BMI calculation below...
You have two options for the units. 
    \nOption 1: Imperial (Height in inches and weight in pounds
Option 2: Metric (Height in metres and weight in kilograms)
    \nWhich option do you choose? Enter 1 for Imperial or 2 for Metric: 
        
    """)

    # validate unit
    if unit not in ['1', '2']:
        print("Invalid unit. Please enter either '1' or '2'.")
        continue

    def correct_float(prompt):
        while True:
            try:
                value = float(input(prompt))
                if value <= 0:
                    print("Please enter a positive number.")
                    continue
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

     # Ask for height and weight based on unit
    if unit == '1':
        height = correct_float("Enter your height in inches: ")
        weight = correct_float("Enter your weight in pounds: ")
        bmi = (weight / (height ** 2)) * 703
    elif unit == '2':
        height = correct_float("Enter your height in metres: ")
        weight = correct_float("Enter your weight in kilograms: ")
        bmi = weight / (height ** 2)

    # Display result
    print(f"\nYour BMI is {bmi:.2f}")
    break
