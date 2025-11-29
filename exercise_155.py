# Exercise 155: Gender Neutral Names

# Some names, like Ben and Jonathan, are normally only used for boys while names
# like Rebbecca and Flora are normally only used for girls. Other names, like Chris
# and Alex, may be used for both boys and girls.
# Write a program that determines and displays all of the baby names that were
# used for both boys and girls in a year specified by the user. Your program should
# generate an appropriate message if there were no gender neutral names in the selected
# year. Display an appropriate error message if you do not have data for the year
# requested by the user. Additional details about the baby names data set are included
# in Exercise 154.

# solution

import os
import re


def parse_line(line):
    """
    Parse a line to extract (name, maybe_gender, maybe_count).
    Supports common formats:
      - Name,Gender,Count
      - Name,Count
      - Name Count
      - Name<TAB>Count
    Returns: (name_or_None, gender_or_None, count_or_None)
    """
    if not line:
        return (None, None, None)
    s = line.strip()
    if not s:
        return (None, None, None)

    # Remove surrounding quotes if present
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        s = s[1:-1].strip()

    # Try comma-separated tokens first
    parts = [p.strip() for p in s.split(",") if p.strip() != ""]
    if len(parts) >= 3:
        name = parts[0]
        gender_token = parts[1].upper()
        gender = 'M' if gender_token.startswith('M') else (
            'F' if gender_token.startswith('F') else None)
        # extract digits from last part
        count = None
        try:
            count_text = re.sub(r"[^\d]", "", parts[2])
            count = int(count_text) if count_text else None
        except Exception:
            count = None
        return (name, gender, count)
    if len(parts) == 2:
        # Could be Name,Count OR Name,Gender
        left, right = parts
        if re.search(r'\d', right):  # right contains digits → it's likely a count
            try:
                count_text = re.sub(r"[^\d]", "", right)
                count = int(count_text) if count_text else None
            except Exception:
                count = None
            return (left, None, count)
        else:
            # treat right as gender token
            rt = right.upper()
            gender = 'M' if rt.startswith('M') else (
                'F' if rt.startswith('F') else None)
            return (left, gender, None)

    # If no commas, split on whitespace (space or tab). Assume last token is count.
    parts = re.split(r'\s+', s)
    if len(parts) >= 2:
        maybe_count = parts[-1]
        name = " ".join(parts[:-1])
        count = None
        try:
            count_text = re.sub(r"[^\d]", "", maybe_count)
            count = int(count_text) if count_text else None
        except Exception:
            count = None
        return (name, None, count)

    # fallback: try to capture a name-like token and digits
    m_name = re.search(r"[A-Za-z'\-]+", s)
    m_count = re.search(r"(\d+)", s)
    name = m_name.group(0) if m_name else None
    count = int(m_count.group(1)) if m_count else None
    return (name, None, count)


def infer_gender_from_filename(fname):
    """
    Basic rules to guess gender from filename.
    Returns 'M' or 'F' or None.
    """
    fn = fname.lower()
    if any(token in fn for token in ('girl', 'girls', 'female', 'fem')):
        return 'F'
    if any(token in fn for token in ('boy', 'boys', 'male', 'm')):
        return 'M'
    # not decisive
    return None


def collect_names_from_file(path):
    """
    Read a file and return a set of names found in that file (cleaned).
    Names are normalized to lowercase to allow case-insensitive matching.
    """
    names = set()
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            for raw in f:
                name, gender, count = parse_line(raw)
                if not name:
                    continue
                # normalize: strip and lower (so 'Chris' and 'chris' match)
                name_clean = name.strip().lower()
                if name_clean:
                    names.add(name_clean)
    except FileNotFoundError:
        pass
    return names


def find_year_files(folder, year_str):
    """
    Return two lists: (boys_files, girls_files, other_files_for_year)
    based on filename containing the year_str. This does not rely solely on filename
    gender detection — it simply collects candidate files for that year.
    """
    boys = []
    girls = []
    others = []
    for fname in os.listdir(folder):
        if year_str in fname:
            full = os.path.join(folder, fname)
            if not os.path.isfile(full):
                continue
            # skip obvious non-data files
            if fname.startswith('.') or fname.lower().endswith(('.md', '.pdf', '.zip')):
                continue
            guessed = infer_gender_from_filename(fname)
            if guessed == 'M':
                boys.append(full)
            elif guessed == 'F':
                girls.append(full)
            else:
                others.append(full)
    return boys, girls, others


def main():
    folder = input(
        "Enter path to folder containing the baby-names files: ").strip()
    if not os.path.isdir(folder):
        print("Folder not found. Please check the path and try again.")
        return

    year = input("Enter the year you want to examine (e.g., 1998): ").strip()
    # basic validation: year should be 4 digits
    if not re.fullmatch(r"\d{4}", year):
        print("Please enter a valid 4-digit year (e.g., 2005).")
        return

    boys_files, girls_files, other_files = find_year_files(folder, year)

    # If we didn't find explicit boys/girls files, try to use 'other_files' by inspecting contents
    if not boys_files and not girls_files and not other_files:
        print(
            f"No data files found in '{folder}' containing the year '{year}'.")
        return

    # If we have 'other' files but not separated by gender, inspect them and classify by content
    if not boys_files or not girls_files:
        # try to classify the 'others' by checking for gender tokens in lines
        for path in other_files:
            # read a few lines to try to detect gender tokens
            male_count = 0
            female_count = 0
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    for i, raw in enumerate(f):
                        if i > 200:  # only sample the first 200 lines to save time
                            break
                        _, gender_token, _ = parse_line(raw)
                        if gender_token == 'M':
                            male_count += 1
                        elif gender_token == 'F':
                            female_count += 1
            except Exception:
                pass
            if male_count > female_count:
                boys_files.append(path)
            elif female_count > male_count:
                girls_files.append(path)
            else:
                # if still undecided, try filename hints
                guessed = infer_gender_from_filename(os.path.basename(path))
                if guessed == 'M':
                    boys_files.append(path)
                elif guessed == 'F':
                    girls_files.append(path)

    # If after all attempts we still don't have both genders, inform the user
    if not boys_files and not girls_files:
        print(f"No files found for year {year}.")
        return
    if not boys_files:
        print(f"No boys file found for year {year}.")
        # even if boys missing, we can still mention girls count, but the exercise requires both
        return
    if not girls_files:
        print(f"No girls file found for year {year}.")
        return

    # Collect names from the files (merge multiple files if more than one)
    boys_names = set()
    for bf in boys_files:
        boys_names.update(collect_names_from_file(bf))

    girls_names = set()
    for gf in girls_files:
        girls_names.update(collect_names_from_file(gf))

    # Intersection: names present in both sets (gender-neutral names for that year)
    neutral = sorted(boys_names.intersection(girls_names))

    if not neutral:
        print(
            f"No gender-neutral names (used for both boys and girls) were found in {year}.")
    else:
        print(
            f"Names used for BOTH boys and girls in {year} (case-insensitive):")
        for name in neutral:
            # print names in a readable capitalization form: capitalize first letter
            print(" -", name.capitalize())
        print(f"\nTotal: {len(neutral)} name(s)")


if __name__ == "__main__":
    main()
