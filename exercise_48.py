# Exercise 48: Chinese Zodiac

# The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is
# shown in the table below. The pattern repeats from there, with 2012 being another
# year of the dragon, and 1999 being another year of the hare.

# Year Animal
# 2000 Dragon
# 2001 Snake
# 2002 Horse
# 2003 Sheep
# 2004 Monkey
# 2005 Rooster
# 2006 Dog
# 2007 Pig
# 2008 Rat
# 2009 Ox
# 2010 Tiger
# 2011 Hare
# Write a program that reads a year from the user and displays the animal associated
# with that year. Your program should work correctly for any year greater than or equal
# to zero, not just the ones listed in the table.

# solution:

def get_chinese_zodiac(year):
    # List of chinese zodiac animals in order
    zodiac_animals = ["Dragon", "Snake", "Horse", "Sheep", "Monkey",
                      "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Hare"]

    # calculate the index in the 12-year cycle
    # 2000 is the year of the dragon (index 0)
    index = (year - 2000) % 12
    return zodiac_animals[index]


def main():
    while True:
        try:
            # prompt the user for a year
            year = int(input("\nEnter a year (>= 0): "))

            # validate that the year is non-negative

            if year < 0:
                print("Please enter a year greater than or equal to 0.")
                continue

            # get the corresponding Chinese zodiac animal

            animal = get_chinese_zodiac(year)
            print(
                f"\nThe Chinese zodiac animal for the year {year} is the {animal}.")
            break  # Exit the loop after successful execution

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()
