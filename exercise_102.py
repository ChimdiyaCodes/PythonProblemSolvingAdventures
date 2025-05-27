# Exercise 102: Reduce Measures

# Many recipe books still use cups, tablespoons and teaspoons to describe the volumes
# of ingredients used when cooking or baking. While such recipes are easy enough to
# follow if you have the appropriate measuring cups and spoons, they can be difficult
# to double, triple or quadruple when cooking Christmas dinner for the entire extended
# family. For example, a recipe that calls for 4 tablespoons of an ingredient requires 16
# tablespoons when quadrupled. However, 16 tablespoons would be better expressed
# (and easier to measure) as 1 cup.
# Write a function that expresses an imperial volume using the largest units pos￾sible. The function will take the number of units as its first parameter, and the unit
# of measure (cup, tablespoon or teaspoon) as its second parameter. Return a string
# representing the measure using the largest possible units as the function’s only result.
# For example, if the function is provided with parameters representing 59 teaspoons
# then it should return the string “1 cup, 3 tablespoons, 2 teaspoons”.
# Hint: One cup is equivalent to 16 tablespoons. One tablespoon is equivalent to
# 3 teaspoons.

# solution:

def convert_to_teaspoons(quantity, unit):
    # Convert any imperial unit to teaspoons.
    unit = unit.lower()
    if unit == "cup":
        return quantity * 16 * 3  # 1 cup = 16 tbsp = 48 tsp
    elif unit == "tablespoon":
        return quantity * 3       # 1 tbsp = 3 tsp
    elif unit == "teaspoon":
        return quantity           # Already in tsp
    else:
        raise ValueError("Invalid unit of measurement.")


def reduce_measurement(units, unit_type):
    # Convert the volume into the largest possible imperial units
    total_teaspoons = convert_to_teaspoons(units, unit_type)

    cups = total_teaspoons // 48
    remaining = total_teaspoons % 48

    tablespoons = remaining // 3
    teaspoons = remaining % 3

    parts = []
    if cups:
        parts.append(f"{cups} cup" + ("s" if cups > 1 else ""))
    if tablespoons:
        parts.append(f"{tablespoons} tablespoon" +
                     ("s" if tablespoons > 1 else ""))
    if teaspoons:
        parts.append(f"{teaspoons} teaspoon" + ("s" if teaspoons > 1 else ""))

    return ", ".join(parts) if parts else "0 teaspoons"


def get_positive_integer(prompt):
    # Prompt the user for a positive integer with error handling.
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_valid_unit(prompt):
    # Prompt the user for a valid unit of measure.
    valid_units = ["cup", "tablespoon", "teaspoon"]
    while True:
        unit = input(prompt).strip().lower()
        if unit in valid_units:
            return unit
        else:
            print(
                f"Invalid unit. Please enter one of: {', '.join(valid_units)}")


def main():
    print("\n---This Program Reduces Imperial Measures---")

    units = get_positive_integer("\nEnter the number of units: ")
    unit_type = get_valid_unit(
        "\nEnter the unit (cup, tablespoon, teaspoon): ")

    result = reduce_measurement(units, unit_type)
    print(f"\nReduced measure: {result}")


if __name__ == "__main__":
    main()
