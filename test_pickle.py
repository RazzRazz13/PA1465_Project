import pickle
import random
import hashlib
import sys
from tqdm import tqdm

def hash_pickle(obj):
    data = pickle.dumps(obj)
    return hashlib.sha256(data).hexdigest()

def test_pickle(funct):
    """
    Test the pickle of a single value
    """
    for _ in range(1000):
            value = funct()
            pick1 = hash_pickle(value)
            pick2 = hash_pickle(value)
            assert(pick1 == pick2)

def test_pickle2(funct):
    """
    Test the pickle of a single value
    """
    for _ in range(1000):
            value = funct(50)
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

def generate_close_float():
    """
    Generate a random float
    """
    return random.uniform(-1e-12, 1e-12)

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

def generate_none():
    return None

def generate_bool():
    return random.choice([True, False])


def create_random_nesteddict(length):

    if length <= 1:
        function_choose = [generate_list, generate_complex, generate_integer, generate_bytes, generate_float, generate_bytearray, generate_string, generate_set]
    else:
        function_choose = [create_random_nesteddict, generate_list, generate_complex, generate_integer, generate_bytes, generate_float, generate_bytearray, generate_string, generate_set]

    value = {}
    for _ in range(random.randint(1, length)):
        func = random.choice(function_choose)
        if (func == create_random_nesteddict):
            value[str(random.randint(1, length))] = func(length // 2)
        else:
            value[str(random.randint(1, length))] = func()
    
    return value

def create_random_nestedlist(length):
    if length <= 1:
        function_choose = [generate_list, generate_complex, generate_integer, generate_bytes, generate_float, generate_bytearray, generate_string, generate_set]
    else:
        function_choose = [create_random_nestedlist, generate_list, generate_complex, generate_integer, generate_bytes, generate_float, generate_bytearray, generate_string, generate_set]

    value = []
    for _ in range(random.randint(1, length)):
        func = random.choice(function_choose)
        if func == create_random_nestedlist:
            value.append(func(length // 2))
        else:
            value.append(func())
    
    return value

def generate_test():
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
        data.append(hash_pickle(generate_none()))
        data.append(hash_pickle(create_random_nesteddict(100)))
        data.append(hash_pickle(create_random_nestedlist(100)))
        data.append(hash_pickle(generate_close_float()))
    return data


def generate_pickle():
    """Skapa pickle-fil unik för denna miljö"""
    platforms = {"win32": "windows-latest", "darwin": "macos-latest", "linux": "ubuntu-latest"}

    filename = f"pickle_py{sys.version_info.major}.{sys.version_info.minor}_{platforms[sys.platform]}.txt"
    with open(filename, "w") as f:
        data = generate_test()
        for item in data:
            f.write(f"{item}\n")
    print(f"Generated: {filename}")

def main():
    random.seed(9001)
    # for _ in tqdm(range(10)):
    #     test_pickle(generate_dict)
    #     test_pickle(generate_string)
    #     test_pickle(generate_set)
    #     test_pickle(generate_bytearray)
    #     test_pickle(generate_bytes)
    #     test_pickle(generate_complex)
    #     test_pickle(generate_float)
    #     test_pickle(generate_integer)
    #     test_pickle(generate_tuple)
    #     test_pickle(generate_close_float)
    #     test_pickle(generate_bool)
    #     test_pickle(generate_none)
    #     test_pickle2(create_random_nesteddict)
    #     test_pickle2(create_random_nestedlist)


    generate_pickle()
    

if __name__ == "__main__":
    main()