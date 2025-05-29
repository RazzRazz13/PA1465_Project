import pickle
import random
import hashlib
import sys
from tqdm import tqdm

def hash_pickle(obj):
    """
    Pickles and hash the input object
    """
    data = pickle.dumps(obj)
    return hashlib.sha256(data).hexdigest()

def generate_tuple():
    """
    Generate a random tuple of values
    """
    data = ()
    for _ in range(random.randint(1, 10)):
        data += (random.randint(1, 10),)
    return data

def generate_list():
    """
    Generate a random list of values
    """
    data = []
    for _ in range(random.randint(1, 10)):
        data.append(random.randint(1, 10))
    return data

def generate_integer():
    """
    Generate a random int
    """
    return random.randint(-10000, 10000)

def generate_float():
    """
    Generate a random float
    """
    return random.uniform(-10000.0, 10000.0)

def generate_close_float():
    """
    Generate a random float
    """
    return random.uniform(-1e-12, 1e-12)

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
    return ''.join(random.choices("abcdefghijklmnopqrstuvwxyzåäö", k=random.randint(5, 10)))

def generate_set():
    """
    Generate a random set
    """
    return {generate_integer() for _ in range(random.randint(2, 5))}

def generate_dict():
    """
    Generate a random dict of values
    """
    data = {}
    for _ in range(random.randint(1, 10)):
        data[random.randint(1, 10)] = random.randint(1, 10)
    return data

def generate_none():
    """
    Generate a none
    """
    return None

def generate_bool():
    """
    Generate a bool
    """
    return random.choice([True, False])

def generate_function():
    """
    Generate a function
    """
    return generate_bool


def generate_nested_dict(length):
    """
    Generate a nested dict
    """
    if length <= 1:
        function_choose = [generate_list, generate_complex, generate_integer, generate_bytes, generate_float, generate_bytearray, generate_string, generate_set]
    else:
        function_choose = [generate_nested_dict, generate_list, generate_complex, generate_integer, generate_bytes, generate_float, generate_bytearray, generate_string, generate_set]

    value = {}
    for _ in range(random.randint(1, length)):
        func = random.choice(function_choose)
        if (func == generate_nested_dict):
            value[str(random.randint(1, length))] = func(length // 2)
        else:
            value[str(random.randint(1, length))] = func()
    
    return value

def generate_nested_list(length):
    """
    Generate a nested list
    """
    if length <= 1:
        function_choose = [generate_list, generate_complex, generate_integer, generate_bytes, generate_float, generate_bytearray, generate_string, generate_set]
    else:
        function_choose = [generate_nested_list, generate_list, generate_complex, generate_integer, generate_bytes, generate_float, generate_bytearray, generate_string, generate_set]

    value = []
    for _ in range(random.randint(1, length)):
        func = random.choice(function_choose)
        if func == generate_nested_list:
            value.append(func(length // 2))
        else:
            value.append(func())
    
    return value

def generate_notimplemented():
    """
    Generate a notimplemented
    """
    return NotImplemented

def generate_ellipsis():
    """
    Generate a ellipsis
    """
    return Ellipsis 

def generate___debug__():
    """
    Generate a __debug__
    """
    return __debug__

def generate_complex():
    """
    Generate a random complex
    """
    return complex(generate_float(), generate_float())

class Dummy:
    def __init__(self, name="Dummy"):
        self.name = name
        self.lamdba = lambda x : x

    def greet(self):
        return self.name

    def __repr__(self):
        return self.lamdba

def generate_class():
    """
    Generate a class object
    """
    return Dummy

def generate_frozenset():
    """
    Generate a frozenset
    """
    return frozenset({generate_integer() for _ in range(10)})

def generate_selfrecursive_dict():
    """
    Generate a selfrecursive dict
    """
    data = {}
    data["self"] = data
    return data

def generate_selfrecursive_list():
    """
    Generate a selfrecursive list
    """
    data = []
    data.append(data)
    return data

def generate_empty_list():
    """
    Generate a empty list
    """
    return []

def generate_empty_dict():
    """
    Generate a empty dict
    """
    return {}

def generate_empty_tuple():
    """
    Generate a empty tuple
    """
    return ()

def generate_empty_set():
    """
    Generate a empty set
    """
    return set()

def generate_empty_bytes():
    """
    Generate empty bytes
    """
    return b""

def generate_mixed_tuple():
    """
    Generate a mixed tuple
    """
    return (generate_integer(), generate_string(), None, generate_bool())

def generate_inf():
    """
    Generate inf
    """
    return float('inf')

def generate_neg_inf():
    """
    Generate -inf
    """
    return float('-inf')

def generate_nan():
    """
    Generate a nan value
    """
    return float('nan')

def generate_test():
    """
    Generate list of testcases
    """
    data = []
    for _ in tqdm(range(1000)):
        data.append(hash_pickle(generate_tuple()))
        data.append(hash_pickle(generate_list()))
        data.append(hash_pickle(generate_integer()))
        data.append(hash_pickle(generate_float()))
        data.append(hash_pickle(generate_complex()))
        data.append(hash_pickle(generate_bytes()))
        data.append(hash_pickle(generate_bytearray()))
        data.append(hash_pickle(generate_string()))
        data.append(hash_pickle(generate_set()))
        data.append(hash_pickle(generate_dict()))
        data.append(hash_pickle(generate_none()))
        data.append(hash_pickle(generate_bool()))
        data.append(hash_pickle(generate_nested_dict(100)))
        data.append(hash_pickle(generate_nested_list(100)))
        data.append(hash_pickle(generate_close_float()))
        data.append(hash_pickle(generate_function()))
        data.append(hash_pickle(generate_notimplemented()))
        data.append(hash_pickle(generate_ellipsis()))
        data.append(hash_pickle(generate___debug__()))
        data.append(hash_pickle(generate_complex()))
        data.append(hash_pickle(generate_class()))
        data.append(hash_pickle(generate_frozenset()))
        data.append(hash_pickle(generate_selfrecursive_dict()))
        data.append(hash_pickle(generate_selfrecursive_list()))
        data.append(hash_pickle(generate_empty_bytes()))
        data.append(hash_pickle(generate_empty_set()))
        data.append(hash_pickle(generate_empty_tuple()))
        data.append(hash_pickle(generate_empty_dict()))
        data.append(hash_pickle(generate_empty_list()))
        data.append(hash_pickle(generate_mixed_tuple()))
        data.append(hash_pickle(generate_inf()))
        data.append(hash_pickle(generate_neg_inf()))
        data.append(hash_pickle(generate_nan()))
    return data


def generate_pickle():
    """Create a pickle file unique of this environment"""
    platforms = {"win32": "windows-latest", "darwin": "macos-latest", "linux": "ubuntu-latest"}

    filename = f"pickle_py{sys.version_info.major}.{sys.version_info.minor}_{platforms[sys.platform]}.txt"
    with open(filename, "w") as f:
        data = generate_test()
        for item in data:
            f.write(f"{item}\n")
    print(f"Generated: {filename}")

def main():
    random.seed(9001)
    generate_pickle()
    

if __name__ == "__main__":
    main()