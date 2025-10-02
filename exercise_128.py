# Exercise 128: Reverse Lookup

# Write a function named reverseLookup that finds all of the keys in a dictionary
# that map to a specific value. The function will take the dictionary and the value to
# search for as its only parameters. It will return a (possibly empty) list of keys from
# the dictionary that map to the provided value.
# Include a main program that demonstrates the reverseLookup function as part
# of your solution to this exercise. Your program should create a dictionary and then
# show that the reverseLookup function works correctly when it returns multiple
# keys, a single key, and no keys. Ensure that your main program only runs when
# the file containing your solution to this exercise has not been imported into another
# program.

def reverseLookup(dictionary, value):
    """
    Find all keys in the dictionary that map to the given value.
    Returns a list of keys (empty if no match).
    """
    result = []
    for key, val in dictionary.items():
        if val == value:
            result.append(key)
    return result


def main():
    # Sample dictionary
    my_dict = {
        "a": 1,
        "b": 2,
        "c": 1,
        "d": 3,
        "e": 2
    }

    # Case 1: Multiple keys
    print("Looking up value 1:", reverseLookup(my_dict, 1))  # ['a', 'c']

    # Case 2: Single key
    print("Looking up value 3:", reverseLookup(my_dict, 3))  # ['d']

    # Case 3: No keys
    print("Looking up value 5:", reverseLookup(my_dict, 5))  # []


if __name__ == "__main__":
    main()
