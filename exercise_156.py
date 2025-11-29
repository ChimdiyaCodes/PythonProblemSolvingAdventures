# Exercise 156: Most Births in a given Time Period

# Write a program that uses the baby names data set described in Exercise 154 to
# determine which names were used most often within a time period. Have the user
# supply the first and last years of the range to analyze. Display the boy’s name and
# the girl’s name given to the most children during the indicated years.

# solution

import os
import re
from collections import defaultdict

# -------------------------
# Helper parsing functions
# -------------------------


def parse_line(line):
    """
    Attempts to parse a single line and return (name_or_None, gender_or_None, count_or_None).
    Tolerant to formats like:
      - Name,Gender,Count
      - Name,Count
      - Name Count
      - Name\tCount
    """
    if not line:
        return (None, None, None)
    s = line.strip()
    if not s:
        return (None, None, None)
    # Remove surrounding quotes
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        s = s[1:-1].strip()

    # Try comma-separated
    parts = [p.strip() for p in s.split(",") if p.strip() != ""]
    if len(parts) >= 3:
        name = parts[0]
        gender_token = parts[1].upper()
        gender = 'M' if gender_token.startswith('M') else (
            'F' if gender_token.startswith('F') else None)
        # extract digits from the count part
        count = None
        try:
            digits = re.sub(r"[^\d]", "", parts[2])
            count = int(digits) if digits else None
        except Exception:
            count = None
        return (name, gender, count)
    if len(parts) == 2:
        left, right = parts
        if re.search(r'\d', right):  # Name,Count
            try:
                digits = re.sub(r"[^\d]", "", right)
                count = int(digits) if digits else None
            except Exception:
                count = None
            return (left, None, count)
        else:  # Name,Gender
            rt = right.upper()
            gender = 'M' if rt.startswith('M') else (
                'F' if rt.startswith('F') else None)
            return (left, gender, None)

    # whitespace-separated fallback
    tokens = re.split(r'\s+', s)
    if len(tokens) >= 2:
        maybe_count = tokens[-1]
        name = " ".join(tokens[:-1])
        try:
            digits = re.sub(r"[^\d]", "", maybe_count)
            count = int(digits) if digits else None
        except Exception:
            count = None
        return (name, None, count)

    # last resort: regex
    m_name = re.search(r"[A-Za-z'\-]+", s)
    m_count = re.search(r"(\d+)", s)
    name = m_name.group(0) if m_name else None
    count = int(m_count.group(1)) if m_count else None
    return (name, None, count)


def infer_gender_from_filename(fname):
    """
    Heuristic to guess whether a filename relates to boys or girls.
    Returns 'M', 'F', or None.
    """
    fn = fname.lower()
    if any(tok in fn for tok in ('girl', 'girls', 'female', 'fem')):
        return 'F'
    if any(tok in fn for tok in ('boy', 'boys', 'male', 'males')):
        return 'M'
    return None

# -------------------------
# File and aggregation helpers
# -------------------------


def collect_counts_from_file(path):
    """
    Returns a dict mapping name_lower -> (total_count_from_file, sample_original_name)
    sample_original_name allows nicer capitalization display later.
    """
    counts = defaultdict(int)
    sample_name = {}
    try:
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            for raw in f:
                name, gender, count = parse_line(raw)
                if not name:
                    continue
                if count is None:
                    continue
                key = name.strip().lower()
                if key == "":
                    continue
                counts[key] += count
                # keep one example of original capitalization
                if key not in sample_name:
                    sample_name[key] = name.strip()
    except FileNotFoundError:
        pass
    return counts, sample_name


def find_files_for_year_range(folder, start_year, end_year):
    """
    Return a list of file paths in folder that appear to belong to any year in [start_year, end_year].
    The check is a simple substring match of the year (e.g., '1998' in filename).
    """
    candidates = []
    for fname in sorted(os.listdir(folder)):
        if fname.startswith('.') or fname.lower().endswith(('.md', '.pdf', '.zip')):
            continue
        for y in range(start_year, end_year + 1):
            if str(y) in fname:
                full = os.path.join(folder, fname)
                if os.path.isfile(full):
                    candidates.append(full)
                    break
    return candidates

# -------------------------
# Main program logic
# -------------------------


def main():
    folder = input(
        "Enter path to the folder containing the baby-name files: ").strip()
    if not os.path.isdir(folder):
        print("Folder not found. Please check the path and try again.")
        return

    start = input("Enter the start year (e.g., 1990): ").strip()
    end = input("Enter the end year (e.g., 1999): ").strip()
    if not (re.fullmatch(r"\d{4}", start) and re.fullmatch(r"\d{4}", end)):
        print("Please enter valid 4-digit years.")
        return
    start_year = int(start)
    end_year = int(end)
    if end_year < start_year:
        print("End year must be the same or later than start year.")
        return

    # find candidate files for the range
    files = find_files_for_year_range(folder, start_year, end_year)
    if not files:
        print(
            f"No files found in '{folder}' for years {start_year}-{end_year}.")
        return

    # two accumulators for totals across the time range
    boys_totals = defaultdict(int)   # name_lower -> total count
    girls_totals = defaultdict(int)
    sample_original = {}  # name_lower -> example original capitalization

    skipped_files = []

    for path in files:
        fname = os.path.basename(path)
        guessed = infer_gender_from_filename(fname)
        file_counts, file_sample = collect_counts_from_file(path)

        if not file_counts:
            skipped_files.append((fname, "no parseable counts"))
            continue

        # If gender is known from filename, add all counts to that gender.
        if guessed == 'M':
            for k, v in file_counts.items():
                boys_totals[k] += v
                if k not in sample_original:
                    sample_original[k] = file_sample.get(k, k)
            continue
        if guessed == 'F':
            for k, v in file_counts.items():
                girls_totals[k] += v
                if k not in sample_original:
                    sample_original[k] = file_sample.get(k, k)
            continue

        # If gender unknown from filename, infer from file contents:
        # Sample first N lines for gender tokens. If more M tokens → boys, else if more F → girls, else skip.
        male_markers = 0
        female_markers = 0
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                for i, raw in enumerate(f):
                    if i >= 200:
                        break
                    _, gender_token, _ = parse_line(raw)
                    if gender_token == 'M':
                        male_markers += 1
                    elif gender_token == 'F':
                        female_markers += 1
        except Exception:
            pass

        if male_markers > female_markers:
            for k, v in file_counts.items():
                boys_totals[k] += v
                if k not in sample_original:
                    sample_original[k] = file_sample.get(k, k)
        elif female_markers > male_markers:
            for k, v in file_counts.items():
                girls_totals[k] += v
                if k not in sample_original:
                    sample_original[k] = file_sample.get(k, k)
        else:
            # ambiguous: skip but record
            skipped_files.append((fname, "ambiguous gender"))

    # Now pick the top name(s) for each gender
    def top_names_from_totals(totals_dict):
        if not totals_dict:
            return []
        max_count = max(totals_dict.values())
        winners = [name for name, cnt in totals_dict.items() if cnt ==
                   max_count]
        return winners, max_count

    boy_winners, boy_count = top_names_from_totals(boys_totals)
    girl_winners, girl_count = top_names_from_totals(girls_totals)

    print("\nResults for years {}-{}:".format(start_year, end_year))

    if boy_winners:
        print("\nBoy name(s) given to the most children:")
        for k in sorted(boy_winners):
            display = sample_original.get(k, k).strip()
            # nice capitalization
            print(f" - {display} — {boys_totals[k]:,} total births")
    else:
        print("\nNo boy-name data found for this period.")

    if girl_winners:
        print("\nGirl name(s) given to the most children:")
        for k in sorted(girl_winners):
            display = sample_original.get(k, k).strip()
            print(f" - {display} — {girls_totals[k]:,} total births")
    else:
        print("\nNo girl-name data found for this period.")

    if skipped_files:
        print("\n(Notes: some files were skipped or ambiguous):")
        for fname, reason in skipped_files:
            print(f" - {fname}: {reason}")


if __name__ == "__main__":
    main()
