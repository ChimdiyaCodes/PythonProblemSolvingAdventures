# Exercise 113: Formatting a List

# When writing out a list of items in English, one normally separates the items with
# commas. In addition, the word “and” is normally included before the last item, unless
# the list only contains one item. Consider the following four lists:
# apples
# apples and oranges
# apples, oranges and bananas
# apples, oranges, bananas and lemons
# Write a function that takes a list of strings as its only parameter. Your function
# should return a string that contains all of the items in the list formatted in the manner
# described previously as its only result. While the examples shown previously only
# include lists containing four elements or less, your function should behave correctly
# for lists of any length. Include a main program that reads several items from the user,
# formats them by calling your function, and then displays the result returned by the
# function.

# solution

def format_list(items):
    # Formats a list of strings into a grammatically correct English list.

    if not items:
        return "No items to display."

    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        return ", ".join(items[:-1]) + f" and {items[-1]}"


def main():
    print("Enter items one by one. Press Enter on a blank line to finish.\n")

    items = []

    while True:
        try:
            item = input("Enter an item (or press Enter to finish): ").strip()

            if item == "":
                break  # Blank input ends the loop

            if item:  # Check if item is not empty after stripping
                items.append(item)
            else:
                print("Invalid input. Please enter a non-empty item.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # Format and display the result
    formatted = format_list(items)
    print("\nFormatted list:")
    print(formatted)


# Run the program
if __name__ == "__main__":
    main()
