import pickle
import random
import hashlib
import sys
from tqdm import tqdm

def hash_pickle(obj):
    data = pickle.dumps(obj)
    return hashlib.sha256(data).hexdigest(), data

def test_pickle(funct):
    """
    Test the pickle of a single value
    """
    for _ in range(1000):
            value = funct()
            pick1 = hash_pickle(value)
            pick2 = hash_pickle(value)
    
    assert(pick1 == pick2)

def generate_tuple():
    """
    Generate a random tuple of values
    """
    tuple = ()
    for _ in range(random.randint(1, 10)):
        tuple += (random.randint(1, 10),)
    return tuple

def generate_list():
    """
    Generate a random list of values
    """
    list = []
    for _ in range(random.randint(1, 10)):
        list.append(random.randint(1, 10))
    return list

def generate_integer():
    """
    Generate a random int
    """
    return random.randint(-100, 100)

def generate_float():
    """
    Generate a random float
    """
    return random.uniform(-100.0, 100.0)

def generate_complex():
    """
    Generate a random complex
    """
    return complex(random.uniform(-10, 10), random.uniform(-10, 10))

def generate_bytes():
    """
    Generate a random bytes
    """
    return bytes([random.randint(0, 255) for _ in range(random.randint(5, 10))])

def generate_bytearray():
    """
    Generate a random bytearray
    """
    return bytearray([random.randint(0, 255) for _ in range(random.randint(5, 10))])

def generate_string():
    """
    Generate a random string
    """
    return ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(5, 10)))

def generate_set():
    """
    Generate a random set
    """
    return {generate_integer() for _ in range(random.randint(2, 5))}

def generate_dict():
    """
    Generate a random dict of values
    """
    dict = {}
    for _ in range(random.randint(1, 10)):
        dict[random.randint(1, 10)] = random.randint(1, 10)
    return dict

def generate_test():
    data = [generate_tuple, 
            generate_list, 
            generate_integer, 
            generate_float, 
            generate_complex, 
            generate_bytes, 
            generate_bytearray, 
            generate_string, 
            generate_set, 
            generate_dict]
    return {f"{func.__name__}": func() for func in data}

def generate_pickle():
    """Skapa pickle-fil unik för denna miljö"""
    platforms = {"win32": "windows-latest", "darwin": "macos-latest", "linux": "ubuntu-latest"}

    filename = f"pickle_py{sys.version_info.major}.{sys.version_info.minor}_{platforms[sys.platform]}.pickle"
    with open(filename, "wb") as f:
        pickle.dump(generate_test, f, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"Generated: {filename}")

def main():
    random.seed(9001)
    for _ in tqdm(range(1000)):
        test_pickle(generate_dict)
        test_pickle(generate_string)
        test_pickle(generate_set)
        test_pickle(generate_bytearray)
        test_pickle(generate_bytes)
        test_pickle(generate_complex)
        test_pickle(generate_float)
        test_pickle(generate_integer)
        test_pickle(generate_tuple)

    generate_pickle()
    

if __name__ == "__main__":
    main()