# Exercise 124: Evaluate Postfix

# Evaluating a postfix expression is easier than evaluating an infix expression because it
# does not contain any brackets and there are no operator precedence rules to consider.
# A postfix expression can be evaluated using the following algorithm:
# Create a new empty list, values
# For each token in the postfix expression
# If the token is a number then
# Convert it to an integer and add it to the end of values
# Else
# Remove an item from the end of values and call it right
# Remove an item from the end of values and call it left
# Apply the operator to left and right
# Append the result to the end of values
# Return the first item in values as the value of the expression
# Write a program that reads a mathematical expression in infix form from the user,
# evaluates it, and displays its value. Uses your solutions to Exercises 122 and 123
# along with the algorithm shown above to solve this problem.

# solution

def tokenize(expression):
    # Breaks a math expression string into tokens (numbers, operators, parentheses).
    tokens = []
    i = 0
    length = len(expression)

    while i < length:
        char = expression[i]

        if char.isspace():
            i += 1
            continue

        if char.isdigit() or (char in "+-" and (
                i == 0 or expression[i-1].isspace() or expression[i-1] in "(*^/+-")):
            num = char
            i += 1
            while i < length and expression[i].isdigit():
                num += expression[i]
                i += 1
            tokens.append(num)
            continue

        if char in "+-*/^()":
            tokens.append(char)
            i += 1
            continue

        raise ValueError(f"Unexpected character in expression: '{char}'")

    return tokens


def precedence(op):
    # Return precedence level of operators (higher number = higher precedence).
    if op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op == '^':
        return 3
    return 0


def infix_to_postfix(tokens):
    # Convert infix token list to postfix token list using stack algorithm.
    operators = []
    postfix = []

    for token in tokens:
        if token.lstrip("+-").isdigit():
            postfix.append(token)

        elif token in "+-*/^":
            while (operators and operators[-1] != "(" and
                   precedence(token) <= precedence(operators[-1])):
                postfix.append(operators.pop())
            operators.append(token)

        elif token == "(":
            operators.append(token)

        elif token == ")":
            while operators and operators[-1] != "(":
                postfix.append(operators.pop())
            if not operators:
                raise ValueError("Mismatched parentheses")
            operators.pop()

        else:
            raise ValueError(f"Invalid token found: {token}")

    while operators:
        top = operators.pop()
        if top in "()":
            raise ValueError("Mismatched parentheses")
        postfix.append(top)

    return postfix


def evaluate_postfix(postfix_tokens):
    # Evaluate a postfix expression using a stack.
    values = []

    for token in postfix_tokens:
        if token.lstrip("+-").isdigit():  # number
            values.append(int(token))
        else:  # operator
            right = values.pop()
            left = values.pop()

            if token == '+':
                result = left + right
            elif token == '-':
                result = left - right
            elif token == '*':
                result = left * right
            elif token == '/':
                result = left / right  # floating division
            elif token == '^':
                result = left ** right
            else:
                raise ValueError(f"Unsupported operator: {token}")

            values.append(result)

    return values[0]


def main():
    while True:
        try:
            expr = input(
                "\nEnter a mathematical expression (or 'q' to quit): ").strip()
            if expr.lower() == 'q':
                print("Exiting program.")
                break

            tokens = tokenize(expr)
            print(f"Tokens: {tokens}")

            postfix = infix_to_postfix(tokens)
            print(f"Postfix: {postfix}")

            result = evaluate_postfix(postfix)
            print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
