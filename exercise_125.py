# Exercise 125: Does a List contain a Sublist?

# A sublist is a list that makes up part of a larger list. A sublist may be a list containing
# a single element, multiple elements, or even no elements at all. For example, [1],
# [2], [3] and [4] are all sublists of [1, 2, 3, 4]. The list [2, 3] is also a
# sublist of [1, 2, 3, 4], but [2, 4] is not a sublist [1, 2, 3, 4] because
# the elements 2 and 4 are not adjacent in the longer list. The empty list is a sublist of
# any list. As a result, [] is a sublist of [1, 2, 3, 4]. A list is a sublist of itself,
# meaning that [1, 2, 3, 4] is also a sublist of [1, 2, 3, 4].
# In this exercise you will create a function, isSublist, that determines whether
# or not one list is a sublist of another. Your function should take two lists, larger
# and smaller, as its only parameters. It should return True if and only if smaller
# is a sublist of larger. Write a main program that demonstrates your function.

# solution

def parse_input(user_input):

    if user_input.strip() == "":
        return []

    result = []
    for item in user_input.split(","):
        item = item.strip()
        if item == "":
            continue
        try:
            result.append(int(item))
        except ValueError:
            print(f"⚠️ Warning: '{item}' is not a valid integer, skipping.")
    return result


def isSublist(larger, smaller):
    if smaller == []:
        return True
    if len(smaller) > len(larger):
        return False
    for i in range(len(larger) - len(smaller) + 1):
        if larger[i:i+len(smaller)] == smaller:
            return True
    return False


def main():
    print("\nCheck if one list is a sublist of another.\n")

    larger_input = input("Enter the larger list (comma separated): ")
    larger = parse_input(larger_input)

    smaller_input = input("\nEnter the smaller list (comma separated): ")
    smaller = parse_input(smaller_input)

    result = isSublist(larger, smaller)
    print(f"\nResult: Is {smaller} a sublist of {larger}? {result}")


if __name__ == "__main__":
    main()
