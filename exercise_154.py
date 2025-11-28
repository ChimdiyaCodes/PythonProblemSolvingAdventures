# Exercise 154: Names that Reached Number One

# The baby names data set consists of over 200 files. Each file contains a list of 100
# names, along with the number of times each name was used. There are two files for
# each year: one containing names used for girls and the other containing names used
# for boys. The data set includes data for every year from 1900 to 2012.
# Write a program that reads every file in the data set and identifies all of the names
# that were most popular in at least one year. Your program should output two lists:
# one containing the most popular names for boys and the other containing the most
# popular names for girls. Neither of your lists should include any repeated values.

# soltuion

#!/usr/bin/env python3

import os
import re
from collections import defaultdict


def parse_line(line):
    """
    Try to extract (name, gender_or_none, count_or_none) from a single line.
    Supports several common formats:
      - Name,Gender,Count
      - Name,Count
      - Name Count
      - Name<TAB>Count
    Returns (name: str or None, gender: 'M'/'F'/None, count: int or None)
    """
    line = line.strip()
    if not line:
        return (None, None, None)

    # Remove surrounding quotes if present
    if (line.startswith('"') and line.endswith('"')) or (line.startswith("'") and line.endswith("'")):
        line = line[1:-1]

    # Try comma-separated first
    parts = [p.strip() for p in line.split(",") if p.strip() != ""]
    if len(parts) >= 3:
        # Name, Gender, Count (or variants)
        name = parts[0]
        gender = parts[1].upper()
        # normalize gender
        if gender.startswith('M'):
            gender = 'M'
        elif gender.startswith('F'):
            gender = 'F'
        else:
            gender = None
        # attempt count from last part
        count = None
        try:
            count = int(re.sub(r"[^\d]", "", parts[2])) if parts[2] else None
        except ValueError:
            count = None
        return (name, gender, count)
    elif len(parts) == 2:
        # Could be Name,Count or Name,Gender
        left, right = parts
        # If right looks like a number -> Name,Count
        if re.search(r'\d', right):
            try:
                count = int(re.sub(r"[^\d]", "", right))
            except ValueError:
                count = None
            return (left, None, count)
        else:
            # Name,Gender (unlikely for this dataset), treat right as gender
            gender = right.upper()
            if gender.startswith('M'):
                gender = 'M'
            elif gender.startswith('F'):
                gender = 'F'
            else:
                gender = None
            return (left, gender, None)

    # If no commas, try splitting by whitespace (space or tab)
    parts = re.split(r'\s+', line)
    if len(parts) >= 2:
        # assume last token is the count
        maybe_count = parts[-1]
        name = " ".join(parts[:-1])
        try:
            count = int(re.sub(r"[^\d]", "", maybe_count))
        except ValueError:
            count = None
        return (name, None, count)

    # If nothing matched, try to extract name-like token and digits
    m_name = re.search(r"[A-Za-z'\-]+", line)
    m_count = re.search(r"(\d+)", line)
    name = m_name.group(0) if m_name else None
    count = int(m_count.group(1)) if m_count else None
    return (name, None, count)


def infer_gender_from_filename(filename):
    """
    Naive rule-based inference from filename (lowercased).
    Returns 'M' / 'F' / None
    """
    fn = filename.lower()
    if 'girl' in fn or 'female' in fn or 'girls' in fn or 'fem' in fn:
        return 'F'
    if 'boy' in fn or 'male' in fn or 'boys' in fn:
        return 'M'
    # many datasets use 'yob' (year of birth) without gender; return None to let per-line parsing decide
    return None


def process_file(path):
    """
    Process one file. Returns a tuple: (gender_detected, set_of_top_names)
    gender_detected is 'M' or 'F' or None (if cannot be determined).
    set_of_top_names: names (strings) that had the maximum count in this file (may be multiple if tied).
    """
    per_name_counts = {}
    genders_observed = defaultdict(int)
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        for raw in f:
            name, gender, count = parse_line(raw)
            if not name:
                continue
            # normalize name trimming whitespace and lowercasing for consistent counting
            name_clean = name.strip()
            # observe gender if present
            if gender in ('M', 'F'):
                genders_observed[gender] += 1
            # store count if available
            if count is None:
                # If count missing, we can't judge this line's rank; skip storing a count
                continue
            # if the file uses multiple entries for same name, keep the largest observed count
            prior = per_name_counts.get(name_clean)
            if (prior is None) or (count > prior):
                per_name_counts[name_clean] = count

    # if no counts found (empty file or unparsable) -> return no result
    if not per_name_counts:
        return (None, set())

    # determine top count and names with that count
    max_count = max(per_name_counts.values())
    top_names = {n for n, c in per_name_counts.items() if c == max_count}

    # decide gender for file:
    if genders_observed:
        # choose the gender observed most often in the file lines
        gender_detected = max(genders_observed, key=genders_observed.get)
    else:
        # try from filename
        gender_detected = infer_gender_from_filename(os.path.basename(path))

    return (gender_detected, top_names)


def main():
    folder = input(
        "Enter the path to the folder containing the baby-names files: ").strip()
    if not os.path.isdir(folder):
        print("Folder not found. Please check the path and try again.")
        return

    boys_top = set()
    girls_top = set()
    skipped_files = []

    for fname in sorted(os.listdir(folder)):
        full = os.path.join(folder, fname)
        if not os.path.isfile(full):
            continue
        # optional: skip hidden files
        if fname.startswith('.') or fname.lower().endswith(('.md', '.pdf')):
            continue

        gender, top_names = process_file(full)
        if not top_names:
            # nothing parsed; skip but report
            skipped_files.append((fname, "no parseable name/count"))
            continue

        if gender == 'M':
            boys_top.update(top_names)
        elif gender == 'F':
            girls_top.update(top_names)
        else:
            # unknown gender: we try to guess using filename again and if still unknown, skip and notify
            guessed = infer_gender_from_filename(fname)
            if guessed == 'M':
                boys_top.update(top_names)
            elif guessed == 'F':
                girls_top.update(top_names)
            else:
                skipped_files.append((fname, "unknown gender"))

    # Output results
    print("\n=== Names that reached number one (boys) ===")
    for name in sorted(boys_top):
        print(name)
    print(
        f"Total distinct boy names that were #1 at least once: {len(boys_top)}")

    print("\n=== Names that reached number one (girls) ===")
    for name in sorted(girls_top):
        print(name)
    print(
        f"Total distinct girl names that were #1 at least once: {len(girls_top)}")

    if skipped_files:
        print("\nFiles skipped or partially processed (filename, reason):")
        for fname, reason in skipped_files:
            print(f" - {fname}: {reason}")


if __name__ == "__main__":
    main()
