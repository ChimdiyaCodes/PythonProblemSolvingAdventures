# Exercise 53: Assessing Employees

# At a particular company, employees are rated at the end of each year. The rating scale
# begins at 0.0, with higher values indicating better performance and resulting in larger
# raises. The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values
# between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated
# with each rating is shown in the following table. The amount of an employee’s raise
# is $2400.00 multiplied by their rating.
# Rating Meaning
# 0.0 Unacceptable performance
# 0.4 Acceptable performance
# 0.6 or more Meritorious performance
# Write a program that reads a rating from the user and indicates whether the performance was unacceptable, acceptable or meritorious. The amount of the employee’s
# raise should also be reported. Your program should display an appropriate error
# message if an invalid rating is entered.

def assess_employee_performance():
    while True:
        try:
            # Prompt the user for the rating
            rating = float(
                input("\nEnter the employee's rating (0.0, 0.4, 0.6 or more): "))

            # Validate the rating
            if rating == 0.0:
                performance = "Unacceptable performance"
            elif rating == 0.4:
                performance = "Acceptable performance"
            elif rating >= 0.6:
                performance = "Meritorious performance"
            else:
                # If the rating is invalid, raise an error
                raise ValueError(
                    "Invalid rating. Rating must be 0.0, 0.4, or 0.6 or more.")

            # Calculate the raise amount
            raise_amount = 2400.00 * rating

            # Display the results
            print(f"\nPerformance: {performance}")
            print(f"Raise Amount: ${raise_amount:.2f}")

            # Exit the loop if the input is valid
            break

        except ValueError as e:
            # Handle invalid inputs
            print(f"Error: {e}. Please enter a valid rating.")


# Run the program
assess_employee_performance()
