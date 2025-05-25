import glob

def compare_pickles():
    """Ladda alla textfiler med hashade pickle-värden och jämför rad-för-rad."""
    files = glob.glob("pickle_*.txt")
    print("Filer som jämförs:", files)
    if not files:
        raise ValueError("Inga pickle-filer hittades!")

    # Läs in alla filer och spara deras rader i en lista av listor
    all_lines = []
    for file in files:
        with open(file, 'r') as f:
            lines = f.read().splitlines()  # splitlines() tar bort radslut
            all_lines.append(lines)

    # Kontrollera att alla filer har samma antal rader
    line_counts = [len(lines) for lines in all_lines]
    if len(set(line_counts)) != 1:
        raise ValueError("Filerna har olika antal rader!")

    # Jämför rad för rad
    for line_num in range(line_counts[0]):
        ref_line = all_lines[0][line_num]
        for file_idx in range(1, len(files)):
            if all_lines[file_idx][line_num] != ref_line:
                raise AssertionError(f"Skillnad på rad {line_num + 1} mellan {files[0]} och {files[file_idx]}")

    print("Alla pickle-hashfiler har samma innehåll rad-för-rad!")

if __name__ == "__main__":
    compare_pickles()