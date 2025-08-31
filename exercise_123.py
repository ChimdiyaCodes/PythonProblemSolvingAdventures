# Exercise 123: Infix to Postfix

# Mathematical expressions are often written in infix form, where operators appear
# between the operands on which they act. While this is a common form, it is also
# possible to express mathematical expressions in postfix form, where the operator
# appears after both operands. For example, the infix expression 3+4 is written as
# 34+ in postfix form. One can convert an infix expression to postfix form using
# the following algorithm:
# Create a new empty list, operators
# Create a new empty list, postfix
# For each token in the infix expression
# If the token is an integer then
# Add the token to the end of postfix
# If the token is an operator then
# While operators is not empty and
# the last item in operators is not an open parenthesis and
# precedence(token) < precedence(last item in operators) do
# Remove the last item from operators and add it to postfix
# Add token to the end of operators
# If the token is an open parenthesis then
# Add token to the end of operators
# If the token is a close parenthesis then
# While the last item in operators is not an open parenthesis do
# Remove the last item from operators and add it to postfix
# Remove the open parenthesis from operators
# While operators is not the empty list do
# Remove the last item from operators and add it to postfix
# Return postfix as the result of the algorithm
# Use your solution to Exercise 122 to tokenize a mathematical expression. Then
# use the algorithm above to transform the expression from infix form to postfix form.
# Your code that implements the preceding algorithm should reside in a function that
# takes a list of tokens representing an infix expression as its only parameter. It should
# return a list of tokens representing the equivalent postfix expression as its only result.
# Include a main program that demonstrates your infix to postfix function by reading
# an expression from the user in infix form and displaying it in postfix form.

# The purpose of converting from infix form to postfix form will become apparent
# when you read Exercise 124. You may find your solutions to Exercises 90 and 91
# helpful when completing this problem.
# The algorithms provided in Exercises 123 and 124 do not perform any error
# checking. As a result, you may crash your program or receive incorrect results
# if you provide them with invalid input. These algorithms can be extended to
# detect invalid input and respond to it in a reasonable manner. Doing so is left
# as an independent study exercise for the interested student.

# solution:

def tokenize(expression):
    """Breaks a math expression string into tokens (numbers, operators, parentheses)."""
    tokens = []
    i = 0
    length = len(expression)

    while i < length:
        char = expression[i]

        # Skip whitespace
        if char.isspace():
            i += 1
            continue

        # Handle numbers (with optional leading + or -)
        if char.isdigit() or (char in "+-" and (
                i == 0 or expression[i-1].isspace() or expression[i-1] in "(*^/+-")):
            num = char
            i += 1
            while i < length and expression[i].isdigit():
                num += expression[i]
                i += 1
            tokens.append(num)
            continue

        # Handle operators and parentheses
        if char in "+-*/^()":
            tokens.append(char)
            i += 1
            continue

        # If invalid character
        raise ValueError(f"Unexpected character in expression: '{char}'")

    return tokens


def precedence(op):
    """Return precedence level of operators (higher number = higher precedence)."""
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op == '^':
        return 3
    return 0  # for parentheses or unknowns


def infix_to_postfix(tokens):
    """Convert infix token list to postfix token list using stack algorithm."""
    operators = []
    postfix = []

    for token in tokens:
        if token.lstrip("+-").isdigit():  # If token is a number
            postfix.append(token)

        elif token in "+-*/^":
            # Pop while operators at top have higher/equal precedence
            while (operators and operators[-1] != "(" and
                   precedence(token) <= precedence(operators[-1])):
                postfix.append(operators.pop())
            operators.append(token)

        elif token == "(":
            operators.append(token)

        elif token == ")":
            # Pop until "(" is found
            while operators and operators[-1] != "(":
                postfix.append(operators.pop())
            if not operators:
                raise ValueError("Mismatched parentheses")
            operators.pop()  # Remove "("

        else:
            raise ValueError(f"Invalid token found: {token}")

    # Pop all remaining operators
    while operators:
        top = operators.pop()
        if top in "()":
            raise ValueError("Mismatched parentheses")
        postfix.append(top)

    return postfix


def main():
    while True:
        try:
            expression = input(
                "\nEnter a mathematical expression (or 'q' to quit): ").strip()
            if expression.lower() == 'q':
                print("\nExiting program. Goodbye!")
                break

            tokens = tokenize(expression)
            print(f"\nTokens: {tokens}")

            postfix = infix_to_postfix(tokens)
            print(f"\nPostfix: {postfix}")

        except Exception as e:
            print(f"Error: {e}. Please try again.")


if __name__ == "__main__":
    main()
