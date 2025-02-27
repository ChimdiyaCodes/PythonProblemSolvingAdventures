# Exercise 40: Name that Triangle

# A triangle can be classified based on the lengths of its sides as equilateral, isosceles
# or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
# triangle has two sides that are the same length, and a third side that is a different
# length. If all of the sides have different lengths then the triangle is scalene.
# Write a program that reads the lengths of 3 sides of a triangle from the user.
# Display a message indicating the type of the triangle.

# solution

print("\nYou will be prompted to enter the lengths of each of the 3 sides of your triangle below.")

# Function to classify the triangle


def classify_triangle(side1, side2, side3):
    if side1 == side2 == side3:
        return "equilateral"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "isosceles"
    else:
        return "scalene"


# Main program
while True:
    try:
        # Prompt the user to enter the lengths of the three sides
        side1 = float(input("\nEnter the length of side 1: "))
        side2 = float(input("Enter the length of side 2: "))
        side3 = float(input("Enter the length of side 3: "))

        # Validate that the side lengths are positive
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            print("Error: All side lengths must be positive numbers. Please try again.")
            continue

        # Check if the sides form a valid triangle
        if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
            # Classify the triangle
            triangle_type = classify_triangle(side1, side2, side3)
            print(f"\nYour triangle is {triangle_type}.")
            break
        else:
            print(
                "Error: The given side lengths do not form a valid triangle. Please try again.")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
