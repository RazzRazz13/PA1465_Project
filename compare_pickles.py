import glob
import hashlib

def compare_pickles():
    """Ladda alla pickle-filer och jämför deras innehåll."""
    files = glob.glob("pickle_*.txt")
    print(files)
    if not files:
        raise ValueError("Inga pickle-filer hittades!")

    # Ladda första filen som referens
    f1 = open(files[0], 'r').read()
    f1_lines = f1.split('\n')
    for f1_n, f1_line in enumerate(f1_lines):
        for file in files[1:]:
            f2 = open(file, 'r').read()
            f2_lines = f2.split('\n')
            for f2_n, f2_line in enumerate(f2_lines):
                if f1_n == f2_n:
                    assert f1_line == f2_line, f"Skillnad mellan {files[0]} och {file}"

    print("Alla pickle-filer ger samma data vid uppackning!")

if __name__ == "__main__":
    compare_pickles()