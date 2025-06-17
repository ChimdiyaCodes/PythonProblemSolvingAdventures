# Exercise 117: Line of Best Fit

# A line of best fit is a straight line that best approximates a collection of n data points.
# In this exercise, we will assume that each point in the collection has an x coordinate
# and a y coordinate. The symbols x¯ and y¯ are used to represent the average x value in  the collection and the average y value in the collection respectively. The line of best
# fit is represented by the equation y = mx + b where m and b are calculated using
# the following formulas:
# m =
# 
# xy − (
#  x)( y)
# n
# 
# x2 − (
#  x)2
# n
# b = ¯y − mx¯
# Write a program that reads a collection of points from the user. The user will enter
# the x part of the first coordinate on its own line, followed by the y part of the first
# coordinate on its own line. Allow the user to continue entering coordinates, with the
# x and y parts each entered on their own line, until your program reads a blank line for
# the x coordinate. Display the formula for the line of best fit in the form y = mx + b
# by replacing m and b with the values you calculated using the preceding formulas.
# For example, if the user inputs the coordinates (1, 1), (2, 2.1) and (3, 2.9) then your
# program should display y = 0.95x + 0.1.

def read_points():
    x_values = []
    y_values = []

    while True:
        try:
            x_input = input("Enter x (or blank to finish): ").strip()
            if x_input == "":
                break
            x = float(x_input)

            y_input = input("Enter y: ").strip()
            y = float(y_input)

            x_values.append(x)
            y_values.append(y)

        except ValueError:
            print("Invalid input. Please enter numeric values for x and y.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")

    return x_values, y_values


def compute_best_fit(x_values, y_values):
    n = len(x_values)

    if n < 2:
        raise ValueError(
            "At least two points are needed to compute a line of best fit.")

    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_xy = sum(x * y for x, y in zip(x_values, y_values))
    sum_x2 = sum(x * x for x in x_values)

    # Compute m
    numerator_m = sum_xy - (sum_x * sum_y) / n
    denominator_m = sum_x2 - (sum_x * sum_x) / n

    if denominator_m == 0:
        raise ValueError(
            "Cannot compute line of best fit because all x values are the same (vertical line).")

    m = numerator_m / denominator_m

    # Compute b
    x_bar = sum_x / n
    y_bar = sum_y / n
    b = y_bar - m * x_bar

    return m, b


def main():
    while True:
        try:
            x_vals, y_vals = read_points()

            if not x_vals:
                print("No points entered. Exiting.")
                break

            m, b = compute_best_fit(x_vals, y_vals)

            print(f"Line of best fit: y = {m:.2f}x + {b:.2f}")
            break

        except ValueError as ve:
            print(f"Error: {ve}\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\n")


# Run the main program
main()
