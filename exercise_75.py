# Exercise 75: Greatest Common Divisor

# The greatest common divisor of two positive integers, n and m, is the largest number,
# d, which divides evenly into both n and m. There are several algorithms that can be
# used to solve this problem, including:
# Initialize d to the smaller of m and n.
# While d does not evenly divide m or d does not evenly divide n do
# Decrease the value of d by 1
# Report d as the greatest common divisor of n and m
# Write a program that reads two positive integers from the user and uses this algorithm
# to determine and report their greatest common divisor.

# solution

def gcd(n, m):
    """
    Calculate the Greatest Common Divisor (GCD) of two positive integers, n and m.
    """
    # Initialize d as the smaller of n and m
    d = min(n, m)

    # Decrement d until it divides both n and m evenly
    while d > 0:
        if n % d == 0 and m % d == 0:
            return d
        d -= 1


def main():
    """
    Main function to handle user input, validation, and GCD calculation.
    """
    while True:
        try:
            # Prompt the user for two positive integers
            n = int(input("\nEnter the first positive integer: "))
            m = int(input("\nEnter the second positive integer: "))

            # Validate that both inputs are positive integers
            if n <= 0 or m <= 0:
                print("Both numbers must be positive integers. Please try again.")
                continue

            # Calculate the GCD
            result = gcd(n, m)

            # Output the result
            print(f"\nThe greatest common divisor of {n} and {m} is: {result}")
            break  # Exit the loop after successful calculation

        except ValueError:
            print("Invalid input. Please enter valid positive integers.")


# Run the program
if __name__ == "__main__":
    main()
