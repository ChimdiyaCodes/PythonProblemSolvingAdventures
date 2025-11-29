# Exercise 169: String Edit Distance

# The edit distance between two strings is a measure of their similarity—the smaller the
# edit distance, the more similar the strings are with regard to the minimum number of
# insert, delete and substitute operations needed to transform one string into the other.
# Consider the strings kitten and sitting. The first string can be transformed
# into the second string with the following operations: Substitute the k with an s,
# substitute the e with an i, and insert a g at the end of the string. This is the smallest
# number of operations that can be performed to transform kitten into sitting.
# As a result, the edit distance is 3.

# Write a recursive function that computes the edit distance between two strings.
# Use the following algorithm:
# Let s and t be the strings
# If the length of s is 0 then
# Return the length of t
# Else if the length of t is 0 then
# Return the length of s
# Else
# Set cost to 0
# If the last character in s does not equal the last character in t then
# Set cost to 1
# Set d1 equal to the edit distance between all characters except the last one
# in s, and all characters in t, plus 1
# Set d2 equal to the edit distance between all characters in s, and all
# characters except the last one in t, plus 1
# Set d3 equal to the edit distance between all characters except the last one
# in s, and all characters except the last one in t, plus cost
# Return the minimum of d1, d2 and d3
# Use your recursive function to write a program that reads two strings from the
# user and displays the edit distance between them.

# solution:

def edit_distance(s, t):
    # Base case 1: If s is empty, distance is len(t)
    if len(s) == 0:
        return len(t)

    # Base case 2: If t is empty, distance is len(s)
    if len(t) == 0:
        return len(s)

    # Determine cost of substituting the last character
    cost = 0
    if s[-1] != t[-1]:
        cost = 1

    # d1 = delete last char from s
    d1 = edit_distance(s[:-1], t) + 1

    # d2 = delete last char from t (equivalent to insert into s)
    d2 = edit_distance(s, t[:-1]) + 1

    # d3 = substitute last char of s with last char of t (if needed)
    d3 = edit_distance(s[:-1], t[:-1]) + cost

    return min(d1, d2, d3)


# ----- MAIN PROGRAM -----
if __name__ == "__main__":
    s = input("Enter first string: ")
    t = input("Enter second string: ")

    dist = edit_distance(s, t)
    print(f"Edit distance between '{s}' and '{t}' is: {dist}")
