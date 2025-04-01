# Exercise 79: Maximum Integer

# This exercise examines the process of identifying the maximum value in a collection
# of integers. Each of the integers will be randomly selected from the numbers between
# 1 and 100. The collection of integers may contain duplicate values, and some of the
# integers between 1 and 100 may not be present.
# Take a moment and think about how you would handle this problem on paper.
# Many people would check each integer in sequence and ask themself if the number
# that they are currently considering is larger than the largest number that they have seen
# previously. If it is, then they forget the previous maximum number and remember
# the current number as the new maximum number. This is a reasonable approach,
# and will result in the correct answer when the process is performed carefully. If you
# were performing this task, how many times would you expect to need to update the
# maximum value and remember a new number?
# While we can answer the question posed at the end of the previous paragraph using
# probability theory, we are going to explore it by simulating the situation. Create a
# program that begins by selecting a random integer between 1 and 100. Save this
# integer as the maximum number encountered so far. After the initial integer has been
# selected, generate 99 additional random integers between 1 and 100. Check each
# integer as it is generated to see if it is larger than the maximum number encountered
# so far. If it is then your program should update the maximum number encountered
# and count the fact that you performed an update. Display each integer after you
# generate it. Include a notation with those integers which represent a new maximum.
# After you have displayed 100 integers your program should display the maximum value encountered, along with the number of times the maximum value
# was updated during the process. Partial output for the program is shown below,
# with… representing the remaining integers that your program will display. Run your
# program several times. Is the number of updates performed on the maximum value
# what you expected?
# 30
# 74 <= Update
# 58
# 17
# 40
# 37
# 13
# 34
# 46
# 52
# 80 <== Update
# 37
# 97 <== Update
# 45
# 55
# 73
# ...
# The maximum value found was 100
# The maximum value was updated 5 times

# solution:

import random


def find_maximum_integers():
    """
    Simulates finding the maximum value in a collection of 100 random integers between 1 and 100.
    Tracks and displays how many times the maximum value was updated during the process.
    """
    # Initialize variables
    max_value = random.randint(1, 100)
    update_count = 0

    # Display the first number (initial maximum)
    print(f"\n{max_value} <== Initial maximum")

    # Generate and process the remaining 99 numbers
    for i in range(2, 101):
        current_num = random.randint(1, 100)

        # Check if the current number is greater than the current maximum
        if current_num > max_value:
            max_value = current_num
            update_count += 1
            print(f"{current_num} <== Update")
        else:
            print(current_num)

    # Display final results
    print("\nFinal Results:")
    print(f"The maximum value found was {max_value}")
    print(f"The maximum value was updated {update_count} times")

    return max_value, update_count


# Run the simulation
if __name__ == "__main__":
    print("\n--- Maximum Integer Simulation: A program that chooses the maximum Integer in a random group of numbers from 1-100 ---")
    max_val, updates = find_maximum_integers()
