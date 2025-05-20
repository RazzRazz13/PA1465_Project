import pickle
import glob

def compare_pickles():
    """Ladda alla pickle-filer och jämför deras innehåll."""
    files = glob.glob("pickle_*.pickle")
    if not files:
        raise ValueError("Inga pickle-filer hittades!")

    # Ladda första filen som referens
    with open(files[0], "rb") as f:
        reference_data = pickle.load(f)

    # Jämför med alla andra filer
    for file in files[1:]:
        with open(file, "rb") as f:
            data = pickle.load(f)
        assert data == reference_data, f"Skillnad mellan {files[0]} och {file}"

    print("Alla pickle-filer ger samma data vid uppackning!")

if __name__ == "__main__":
    compare_pickles()