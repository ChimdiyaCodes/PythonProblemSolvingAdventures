# Exercise 133:Write Out Numbers in English

# While the popularity of cheques as a payment method has diminished in recent years,
# some companies still issue them to pay employees or vendors. The amount being
# paid normally appears on a cheque twice, with one occurrence written using digits,
# and the other occurrence written using English words. Repeating the amount in two
# different forms makes it much more difficult for an unscrupulous employee or vendor
# to modify the amount on the cheque before depositing it.
# In this exercise, your task is to create a function that takes an integer between 0 and
# 999 as its only parameter, and returns a string containing the English words for that
# number. For example, if the parameter to the function is 142 then your function should
# return “one hundred forty two”. Use one or more dictionaries to implement
# your solution rather than large if/elif/else constructs. Include a main program that
# reads an integer from the user and displays its value in English words.

# solution

def number_to_words(num):
    # Dictionaries for word mappings
    ones = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "fifteen", 16: "sixteen",
        17: "seventeen", 18: "eighteen", 19: "nineteen"
    }

    tens = {
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }

    # Handle 0–19
    if num < 20:
        return ones[num]

    # Handle 20–99
    elif num < 100:
        ten_part = (num // 10) * 10
        one_part = num % 10
        if one_part == 0:
            return tens[ten_part]
        else:
            return f"{tens[ten_part]} {ones[one_part]}"

    # Handle 100–999
    else:
        hundred_part = num // 100
        remainder = num % 100
        if remainder == 0:
            return f"{ones[hundred_part]} hundred"
        else:
            return f"{ones[hundred_part]} hundred {number_to_words(remainder)}"


def main():
    while True:
        try:
            user_input = input(
                "\nEnter an integer between 0 and 999: ").strip()

            # Check if input is numeric
            if not user_input.isdigit():
                raise ValueError("Input must be a number.")

            number = int(user_input)

            # Validate range
            if number < 0 or number > 999:
                raise ValueError("Number must be between 0 and 999.")

            # Convert and display
            print(f"\nIn words: {number_to_words(number)}")
            break

        except ValueError as e:
            print(f"Error: {e}. Please try again.\n")


if __name__ == "__main__":
    main()
