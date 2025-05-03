# Exercise 88: Is it a Valid Triangle?

# If you have 3 straws, possibly of differing lengths, it may or may not be possible
# to lay them down so that they form a triangle when their ends are touching. For
# example, if all of the straws have a length of 6 inches. then one can easily construct
# an equilateral triangle using them. However, if one straw is 6 inches. long, while the
# other two are each only 2 inches. long, then a triangle cannot be formed. In general,
# if any one length is greater than or equal to the sum of the other two then the lengths
# cannot be used to form a triangle. Otherwise they can form a triangle.
# Write a function that determines whether or not three lengths can form a triangle.
# The function will take 3 parameters and return a Boolean result. In addition, write a
# program that reads 3 lengths from the user and demonstrates the behaviour of this
# function.

# solution

def is_valid_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


def main():
    print("\nThis program allows you check if 3 lengths can form a triangle.")

    while True:
        try:
            # Get user input and convert to floats
            a = float(input("\nEnter the length of side A: ").strip())
            b = float(input("Enter the length of side B: ").strip())
            c = float(input("Enter the length of side C: ").strip())

            # Validate that all sides are positive
            if a <= 0 or b <= 0 or c <= 0:
                raise ValueError(
                    "All side lengths must be positive numbers greater than zero.")

            break  # Exit the loop if everything is valid

        except ValueError as e:
            print(f"Input error: {e}. Please try again.")

    # Call the triangle validation function
    if is_valid_triangle(a, b, c):
        print("\n✅ Welldone, these lengths can form a triangle.")
    else:
        print("\n❌ Please, try again. These lengths cannot form a triangle.")


# Only run main if this file is executed directly
if __name__ == "__main__":
    main()
