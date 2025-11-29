# Exercise 165: Greatest Common Divisor

# Euclid was a Greek mathematician who lived approximately 2,300 years ago. His
# algorithm for computing the greatest common divisor of two positive integers, a and
# b, is both efficient and recursive. It is outlined below:
# If b is 0 then
# Return a
# Else
# Set c equal to the remainder when a is divided by b
# Return the greatest common divisor of b and c
# Write a program that implements Euclid’s algorithm and uses it to determine the
# greatest common divisor of two integers entered by the user.

def gcd(a, b):
    """
    Recursive function to compute the Greatest Common Divisor (GCD) of two integers.
    """
    if b == 0:
        return a
    else:
        remainder = a % b
        return gcd(b, remainder)


def main():
    print("Compute the Greatest Common Divisor (GCD) of two positive integers.")

    while True:
        try:
            a = int(input("Enter the first positive integer: ").strip())
            b = int(input("Enter the second positive integer: ").strip())
            if a <= 0 or b <= 0:
                print("Both numbers must be positive integers. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter positive integers.")

    result = gcd(a, b)
    print(f"The greatest common divisor of {a} and {b} is: {result}")


if __name__ == "__main__":
    main()
