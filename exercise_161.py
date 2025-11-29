# Exercise 161: Missing Comments

# When one writes a function, it is generally a good idea to include a comment that
# outlines the function’s purpose, its parameters and its return value. However, some￾times comments are forgotten, or left out by well-intentioned programmers that plan
# to write them later but then never get around to it.
# Create a python program that reads one or more Python source files and identifies
# functions that are not immediately preceded by a comment. For the purposes of this
# exercise, assume that any line that begins with def, followed by a space, is the

# beginning of a function definition. Assume that the comment character, #, will be
# the first character on the previous line when the function has a comment. Display the
# names of all of the functions that are missing comments, along with the file name
# and line number where the function definition is located.
# The user will provide the names of one or more Python files as command line
# parameters. If your program encounters a file that doesn’t exist or can’t be opened
# then it should display an appropriate error message before moving on and processing
# the remaining files.

# solution

import sys


def extract_function_name(def_line):
    """
    Given a line that begins with 'def ', extract the function name.
    Example: "def my_func(a, b):" -> "my_func"
    This is conservative: it takes the text after 'def ' up to the first '('
    or the first ':' if '(' is missing.
    """
    # remove the leading 'def ' (we assume the caller already checked it begins with 'def ')
    rest = def_line[len("def "):].strip()
    # function name is before the first '(' if present
    paren_index = rest.find('(')
    if paren_index != -1:
        name = rest[:paren_index].strip()
    else:
        # fallback: before the first ':' or the whole rest if neither exists
        colon_index = rest.find(':')
        if colon_index != -1:
            name = rest[:colon_index].strip()
        else:
            name = rest.split()[0] if rest.split() else ""
    return name


def check_file(filename):
    """
    Check a single file for functions that are not immediately preceded
    by a comment line whose first character is '#'.
    Returns a list of tuples: (line_number, function_name).
    """
    missing = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File not found: {filename}")
        return None
    except PermissionError:
        print(f"Error: Permission denied when trying to open: {filename}")
        return None
    except Exception as e:
        print(f"Error: Could not open {filename}: {e}")
        return None

    # iterate over lines with index so we can examine the previous line
    for idx, line in enumerate(lines):
        # we check for lines that begin exactly with 'def ' (no leading whitespace)
        if line.startswith('def '):
            # get previous line if it exists
            prev_index = idx - 1
            prev_line = lines[prev_index] if prev_index >= 0 else None

            # determine if previous line begins with '#' as its first character
            has_comment = False
            if prev_line is not None:
                # check first character of the previous line
                # strip only trailing newline, don't strip leading spaces: requirement says '#' must be first character
                if prev_line.startswith('#'):
                    has_comment = True

            if not has_comment:
                func_name = extract_function_name(line)
                # record 1-based line number where def appears
                missing.append((idx + 1, func_name))

    return missing


def main():
    if len(sys.argv) < 2:
        print("Usage: python missing_comments.py file1.py [file2.py ...]")
        return

    filenames = sys.argv[1:]

    any_missing = False
    for fname in filenames:
        result = check_file(fname)
        if result is None:
            # file open error already printed inside check_file; skip to next
            continue

        if result:
            any_missing = True
            for line_no, func_name in result:
                # func_name could be empty if extraction failed; print what we have
                if func_name:
                    print(
                        f"{fname}: line {line_no}: function '{func_name}' is missing a comment")
                else:
                    print(
                        f"{fname}: line {line_no}: function (name could not be parsed) is missing a comment")

    if not any_missing:
        print("No missing-function-comment issues found in the provided files.")


if __name__ == "__main__":
    main()
