import pickle
import random

def test1(value):
    """Test if pickling + hashing is consistent."""
    # Hash twice and compare
    hash1 = hash(pickle.dumps(value))
    hash2 = hash(pickle.dumps(value))
    assert hash1 == hash2, "Hash mismatch for same input!"

def test2(value):
    """Test if pickle -> unpickle -> pickle produces equivalent data."""
    # Serialize -> deserialize -> serialize again
    pic1 = pickle.dumps(value)
    unpickled = pickle.loads(pic1)
    pic2 = pickle.dumps(unpickled)
    
    # Compare the serialized bytes (should be equal for most cases)
    assert pic1 == pic2, "Serialized data changed after roundtrip!"

def generate_tuple():
    """Generate a random tuple."""
    return tuple(random.randint(1, 1000) for _ in range(random.randint(1, 100)))

def generate_list():
    """Generate a random list."""
    return [random.randint(1, 1000) for _ in range(random.randint(1, 100))]

def generate_dict():
    """Generate a random dict."""
    return {random.randint(1, 100): random.randint(1, 100) for _ in range(random.randint(1, 100))}

def random_data_generator():
    """Yield random data structures indefinitely."""
    generators = [generate_tuple, generate_list, generate_dict]
    while True:
        yield random.choice(generators)()

def main():
    random.seed(9001)
    data_generator = random_data_generator()
    for _ in range(1000):
        data = next(data_generator)
        test1(data)
        test2(data)

if __name__ == "__main__":
    main()