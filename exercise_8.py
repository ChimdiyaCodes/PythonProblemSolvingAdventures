# Exercise 8:Widgets and Gizmos

# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order.

# Solution:

# Define constants for product weights
WIDGET_WEIGHT = 75  # grams
GIZMO_WEIGHT = 112  # grams

try:
    # Get input from user for quantity of each product
    widget_count = int(input("How many widgets did you buy? "))
    gizmo_count = int(input("\nHow many gizmos did you buy? "))

    # Check for negative numbers
    if widget_count < 0 or gizmo_count < 0:
        print("Please enter non-negative numbers.")
    else:
        # Calculate weights for each product type
        widget_total = widget_count * WIDGET_WEIGHT
        gizmo_total = gizmo_count * GIZMO_WEIGHT

        # Calculate total weight of the order
        total_weight = widget_total + gizmo_total

        # Display order summary with detailed breakdown
        print(f"\nOrder Summary:")
        print(f"Widgets: {widget_count} * {WIDGET_WEIGHT}g = {widget_total}g")
        print(f"Gizmos: {gizmo_count} * {GIZMO_WEIGHT}g = {gizmo_total}g")
        print(f"Total weight: {total_weight}g")

except ValueError:
    print("Please enter valid numbers.")
