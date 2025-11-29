# Exercise 173: Run-Length Decoding

# Run-length encoding is a simple data compression technique that can be effec￾tive when repeated values occur at adjacent positions within a list. Compression is  achieved by replacing groups of repeated values with one copy of the value, followed
# by the number of times that the value should be repeated. For example, the list ["A",
# "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B",
# "B", "B", "A", "A", "A", "A", "A", "A", "B"] would be compressed
# as ["A", 12, "B", 4, "A", 6, "B", 1]. Decompression is performed by
# replicating each value in the list the number of times indicated.
# Write a recursive function that decompresses a run-length encoded list. Your
# recursive function will take a run-length compressed list as its only parameter. It will
# return the decompressed list as its only result. Create a main program that displays
# a run-length encoded list and the result of decoding it

# solution

def decode_rle(encoded):
    """
    Recursively decodes a run-length encoded list.
    encoded format: [value, count, value, count, ...]
    """
    # Base case: empty list
    if not encoded:
        return []

    # Extract first pair
    value = encoded[0]
    count = encoded[1]

    # Expand the value 'count' times
    expanded = [value] * count

    # Recursively decode the rest of the list
    return expanded + decode_rle(encoded[2:])


def main():
    encoded_list = ["A", 12, "B", 4, "A", 6, "B", 1]

    print("Run-length encoded list:")
    print(encoded_list)

    decoded_list = decode_rle(encoded_list)

    print("\nDecoded (decompressed) list:")
    print(decoded_list)


# Run the program
if __name__ == "__main__":
    main()
