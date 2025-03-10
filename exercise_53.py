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
