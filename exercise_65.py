# Exercise 65: Compute the Perimeter of a Polygon

# Write a program that computes the perimeter of a polygon. Begin by reading the x
# and y values for the first point on the perimeter of the polygon from the user. Then
# continue reading pairs of x and y values until the user enters a blank line for the x-coordinate. Each time you read an additional coordinate you should compute the
# distance to the previous point and add it to the perimeter. When a blank line is entered
# for the x-coordinate your program should add the distance from the last point back
# to the first point to the perimeter. Then it should display the total perimeter.

# solution:
import math


def get_coordinate(prompt):
    while True:
        try:
            value = input(prompt)
            if value.strip() == "":
                return None
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def main():
    perimeter = 0.0
    points = []

    # Get the first point
    x = get_coordinate("Enter the x part of the coordinate: ")
    if x is None:
        print("No coordinates entered. Exiting.")
        return
    y = get_coordinate("Enter the y part of the coordinate: ")
    if y is None:
        print("No coordinates entered. Exiting.")
        return
    points.append((x, y))

    # Get additional points
    while True:
        x = get_coordinate(
            "Enter the x part of the coordinate: (blank to quit): ")
        if x is None:
            break
        y = get_coordinate("Enter the y part of the coordinate: ")
        if y is None:
            break
        points.append((x, y))

        # Calculate the distance between the current point and the previous point
        prev_x, prev_y = points[-2]
        distance = calculate_distance(prev_x, prev_y, x, y)
        perimeter += distance

    # Calculate the distance from the last point back to the first point
    if len(points) >= 2:
        first_x, first_y = points[0]
        last_x, last_y = points[-1]
        distance = calculate_distance(last_x, last_y, first_x, first_y)
        perimeter += distance

    print(f"The perimeter of that polygon is {perimeter}")


if __name__ == "__main__":
    main()
