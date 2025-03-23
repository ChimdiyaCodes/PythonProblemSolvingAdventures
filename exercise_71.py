# Exercise 71: Square Root

# Write a program that implements Newton’s method to compute and display the square
# root of a number entered by the user. The algorithm for Newton’s method follows:
# Read x from the user
# Initialize guess to x/2
# While guess is not good enough do
# Update guess to be the average of guess and x/guess
# When this algorithm completes, guess contains an approximation of the square
# root. The quality of the approximation depends on how you define “good enough”.
# In the author’s solution, guess was considered good enough when the absolute value
# of the difference between guess ∗ guess and x was less than or equal to 10−12.

# solution:

def compute_square_root():
    while True:
        try:
            # Step 1: Read input from the user
            x = float(
                input("Enter a positive number to compute its square root: "))

            # Step 2: Validate input
            if x < 0:
                print("Error: Please enter a non-negative number.")
                continue  # Restart the loop to get valid input

            # Step 3: Initialize guess
            guess = x / 2.0

            # Step 4: Iterate using Newton's method
            while True:
                # Update guess
                new_guess = (guess + x / guess) / 2.0

                # Check if the guess is good enough
                if abs(new_guess * new_guess - x) <= 1e-12:
                    break  # Exit the loop if the guess is good enough

                guess = new_guess  # Update guess for the next iteration

            # Step 5: Output the result
            print(f"The square root of {x} is approximately {new_guess:.12f}")
            break  # Exit the outer loop after successful computation

        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break


# Call the function to execute the program
compute_square_root()
