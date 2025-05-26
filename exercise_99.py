# Exercise 99: Arbitrary Base Conversions

# Write a program that allows the user to convert a number from one base to another.
# Your program should support bases between 2 and 16 for both the input number and
# the result number. If the user chooses a base outside of this range then an appropriate
# error message should be displayed and the program should exit. Divide your program
# into several functions, including a function that converts from an arbitrary base to
# base 10, a function that converts from base 10 to an arbitrary base, and a main
# program that reads the bases and input number from the user. You may find your
# solutions to Exercises 77, 78 and 98 helpful when completing this exercise.

# solution

def convert_to_base10(number_str, base):
    # Convert a number from any base (2–16) to base 10.
    number_str = number_str.upper()
    digits = '0123456789ABCDEF'
    value = 0

    for character in number_str:
        if character not in digits[:base]:
            raise ValueError(
                f"Invalid character '{character}' for base {base}")
        value = value * base + digits.index(character)
    return value


def convert_from_base10(number_int, base):
    # Convert a base 10 number to any base (2–16).
    if number_int == 0:
        return '0'

    digits = '0123456789ABCDEF'
    result = ''

    while number_int > 0:
        remainder = number_int % base
        result = digits[remainder] + result
        number_int //= base
    return result


def get_valid_base(prompt):
    # Prompt for a base and validate it's between 2 and 16.
    while True:
        try:
            base = int(input(prompt))
            if 2 <= base <= 16:
                return base
            else:
                print("❌ Base must be between 2 and 16.")
        except ValueError:
            print("❌ Please enter a valid integer for the base.")


def get_valid_number(prompt, base):
    # Prompt for a number and ensure it's valid in the given base.
    digits = '0123456789ABCDEF'
    allowed_chars = digits[:base]

    while True:
        number = input(prompt).strip().upper()
        if all(char in allowed_chars for char in number):
            return number
        else:
            print(
                f"❌ Invalid number for base {base}. Allowed digits: {allowed_chars}")


def main():
    print("\n🔁 Arbitrary Base Converter (Supports bases 2–16)")

    # Step 1: Get valid source and target bases
    from_base = get_valid_base("\nEnter the base of the input number (2–16): ")
    to_base = get_valid_base("\nEnter the base to convert to (2–16): ")

    # Step 2: Get valid number in the given base
    number_str = get_valid_number(
        f"\nEnter the number in base {from_base}: ", from_base)

    try:
        # Step 3: Convert to base 10
        base10_value = convert_to_base10(number_str, from_base)

        # Step 4: Convert to target base
        result = convert_from_base10(base10_value, to_base)

        print(f"\n✅ {number_str} (base {from_base}) = {result} (base {to_base})")
    except ValueError as e:
        print(f"❌ Error: {e}")


# Run the program
if __name__ == "__main__":
    main()
