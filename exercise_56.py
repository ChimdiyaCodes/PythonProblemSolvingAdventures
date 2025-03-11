# Exercise 56: Cell Phone Bill

# A particular cell phone plan includes 50 minutes of air time and 50 text messages
# for $15.00 a month. Each additional minute of air time costs $0.25, while additional
# text messages cost $0.15 each. All cell phone bills include an additional charge of
# $0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
# subject to 5 percent sales tax.

# Write a program that reads the number of minutes and text messages used in a
# month from the user. Display the base charge, additional minutes charge (if any),
# additional text message charge (if any), the 911 fee, tax and total bill amount. Only
# display the additional minute and text message charges if the user incurred costs in
# these categories. Ensure that all of the charges are displayed using 2 decimal places.

# solution

def calculate_bill():
    while True:
        try:
            # Input validation for minutes and text messages
            minutes = int(input("\nEnter the number of minutes you used: "))
            texts = int(
                input("\nEnter the number of text messages you used: "))

            if minutes < 0 or texts < 0:
                print("Please enter non-negative numbers.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    # Constants
    BASE_CHARGE = 15.00
    INCLUDED_MINUTES = 50
    INCLUDED_TEXTS = 50
    ADDITIONAL_MINUTE_COST = 0.25
    ADDITIONAL_TEXT_COST = 0.15
    FEE_911 = 0.44
    TAX_RATE = 0.05

    # Calculate additional charges
    additional_minutes = max(0, minutes - INCLUDED_MINUTES)
    additional_texts = max(0, texts - INCLUDED_TEXTS)

    additional_minutes_charge = additional_minutes * ADDITIONAL_MINUTE_COST
    additional_texts_charge = additional_texts * ADDITIONAL_TEXT_COST

    # Calculate subtotal
    subtotal = BASE_CHARGE + additional_minutes_charge + \
        additional_texts_charge + FEE_911

    # Calculate tax
    tax = subtotal * TAX_RATE

    # Calculate total bill
    total_bill = subtotal + tax

    # Display results
    print("\nHere is your Bill Breakdown:")
    print(f"Base Charge: ${BASE_CHARGE:.2f}")
    if additional_minutes > 0:
        print(f"Additional Minutes Charge: ${additional_minutes_charge:.2f}")
    if additional_texts > 0:
        print(f"Additional Texts Charge: ${additional_texts_charge:.2f}")
    print(f"911 Fee: ${FEE_911:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"\nTherefore, your Total Bill is: ${total_bill:.2f}")


# Run the program
if __name__ == "__main__":
    calculate_bill()
