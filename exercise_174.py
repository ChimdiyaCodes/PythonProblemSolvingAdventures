# Exercise 174: Run-Length Encoding

# Write a recursive function that implements the run-length compression technique
# described in Exercise 173. Your function will take a list or a string as its only parameter. It should return the run-length compressed list as its only result. Include a main
# program that reads a string from the user, compresses it, and displays the run-length
# encoded result.
# Hint: You may want to include a loop inside the body of your recursive function.

# solution

def encode_rle(data):
    """
    Recursively encodes a string or list using run-length encoding.
    Returns a list in the format [value, count, value, count, ...]
    """

    # Convert lists to strings for simplicity
    if isinstance(data, list):
        data = "".join(data)

    # Base case: empty string
    if data == "":
        return []

    first = data[0]      # current character
    count = 1            # we have seen it at least once

    # Count repeated characters at the beginning
    i = 1
    while i < len(data) and data[i] == first:
        count += 1
        i += 1

    # Encode this character + recursively encode the rest
    return [first, count] + encode_rle(data[count:])


def main():
    user_input = input("Enter a string to compress: ")

    encoded = encode_rle(user_input)

    print("\nRun-length encoded result:")
    print(encoded)


# Run the program
if __name__ == "__main__":
    main()
