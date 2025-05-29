import glob

def compare_pickles():
    """Compares all files in the directory"""
    files = glob.glob("pickle_*.txt")
    print("Filer som jämförs:", files)
    if not files:
        raise ValueError("Inga pickle-filer hittades!")

    # Reads all files and saves them in list
    all_lines = []
    for file in files:
        with open(file, 'r') as f:
            lines = f.read().splitlines()
            all_lines.append(lines)

    # Check that looks so all files have the same amount of rows
    line_counts = [len(lines) for lines in all_lines]
    if len(set(line_counts)) != 1:
        raise ValueError("Filerna har olika antal rader!")

    # Compare the files row by row
    for line_num in range(line_counts[0]):
        ref_line = all_lines[0][line_num]
        for file_idx in range(1, len(files)):
            if all_lines[file_idx][line_num] != ref_line:
                raise AssertionError(f"Difference on {line_num + 1} between {files[0]} and {files[file_idx]}")

    print("Tests completed")

if __name__ == "__main__":
    compare_pickles()