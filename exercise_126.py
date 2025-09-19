# Exercise 126: Generate All Sublists of a List

# Using the definition of a sublist from Exercise 125, write a function that returns a list
# containing every possible sublist of a list. For example, the sublists of [1, 2, 3]
# are [], [1], [2], [3], [1, 2], [2, 3] and [1, 2, 3]. Note that your function will
# always return a list containing at least the empty list because the empty list
# is a sublist of every list. Include a main program that demonstrate your function by
# displaying all of the sublists of several different lists.

# solution

def all_sublists(lst):
    """
    Generate all possible sublists (consecutive slices)
    of the given list.
    """
    result = [[]]  # Start with the empty list

    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            result.append(sublist)

    return result


if __name__ == "__main__":
    # Ask the user for input
    user_input = input("\nEnter a list of numbers separated by commas: ")

    # Convert input string into a list of integers
    if user_input.strip() == "":
        lst = []  # handle empty input
    else:
        lst = [int(x.strip()) for x in user_input.split(",")]

    # Display the result using f-strings
    print(f"\nAll sublists of {lst}:")
    print(all_sublists(lst))
