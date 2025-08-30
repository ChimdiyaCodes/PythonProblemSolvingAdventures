# Exercise 122: Tokenizing a String

# Tokenizing is the process of converting a string into a list of substrings, known as
# tokens. In many circumstances, a list of tokens is far easier to work with than the
# original string because the original string may have irregular spacing. In some cases
# substantial work is also required to determine where one token ends and the next one
# begins.
# In a mathematical expression, tokens are items such as operators, numbers and
# parentheses. Some tokens, such as *, /, ˆ, ( and ) are easy to identify because the
# token is a single character, and the character is never part of another token. The + and
# - symbols are a little bit more challenging to handle because they might represent
# the addition or subtraction operator, or they might be part of a number token.
# Hint: A + or - is an operator if the non-whitespace character immediately
# before it is part of a number, or if the non-whitespace character immediately
# before it is a close parenthesis. Otherwise it is part of a number.
# Write a function that takes a string containing a mathematical expression as its
# only parameter and breaks it into a list of tokens. Each token should be a parenthesis,
# an operator, or a number with an optional leading + or - (for simplicity we will
# only work with integers in this problem). Return the list of tokens as the function’s
# result.
# You may assume that the string passed to your function always contains a valid
# mathematical expression consisting of parentheses, operators and integers. How￾ever, your function must handle variable amounts of whitespace between these
# elements. Include a main program that demonstrates your tokenizing function by
# reading an expression from the user and printing the list of tokens. Ensure that the
# main program will not run when the file containing your solution is imported into
# another program.

# solution

def tokenize(expression):
    tokens = []
    i = 0
    length = len(expression)

    while i < length:
        char = expression[i]

        # Skip whitespace
        if char.isspace():
            i += 1
            continue

        # Handle numbers (possibly with leading + or -)
        if char.isdigit() or (char in "+-" and (i == 0 or expression[i-1].isspace() or expression[i-1] in "(*^/+-")):

            # Start building the number
            num = char
            i += 1
            while i < length and expression[i].isdigit():
                num += expression[i]
                i += 1
            tokens.append(num)
            continue  # move to next character

        # Handle operators and parentheses
        if char in "+-*/^()":
            tokens.append(char)
            i += 1
            continue

        # If an unknown character is found
        raise ValueError(f"Unexpected character in expression: '{char}'")

    return tokens


def main():
    while True:
        try:
            expr = input("\nEnter a mathematical expression: ").strip()
            if not expr:
                print("Expression cannot be empty. Try again.")
                continue

            tokens = tokenize(expr)
            print(f"\nThe list of tokens is: {tokens}")
            break

        except ValueError as e:
            print(f"Error: {e}. Please try again.")

        except KeyboardInterrupt:
            print("\nProgram exited by user.")
            break


if __name__ == "__main__":
    main()
