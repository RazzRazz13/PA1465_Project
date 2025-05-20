import pickle
import glob
import hashlib

def compare_pickles():
    """Ladda alla pickle-filer och jämför deras innehåll."""
    files = glob.glob("pickle_*.pickle")
    if not files:
        raise ValueError("Inga pickle-filer hittades!")

    # Ladda första filen som referens
    expected_hash = hashlib.sha256(open(files[0], 'rb').read()).hexdigest()

    # Jämför med alla andra filer
    for file in files[1:]:
        reference_hash = hashlib.sha256(open(file, 'rb').read()).hexdigest()
        assert expected_hash == reference_hash, f"Skillnad mellan {files[0]} och {file}"

    print("Alla pickle-filer ger samma data vid uppackning!")

if __name__ == "__main__":
    compare_pickles()