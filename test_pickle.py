import pickle
import random
from tqdm import tqdm

def test1(value):
    """
    Test the pickle and unpickle of a single value
    """
    for _ in range(random.randint(1, 1000)):
        if random.randint(0, 1) == 0:
            pic = pickle.dumps(value)
            unpickle = pickle.loads(pic)
        else:
            pic = pickle.dump(value)
            unpickle = pickle.load(pic)
    
    assert(value == unpickle)

def test2(value):
    """
    Test the pickel object of a single value
    """
    if random.randint(0, 1) == 0:
        pic1 = pickle.dumps(value)
        unpickle = pickle.loads(pic1)
        pic2 = pickle.dumps(unpickle)
    else:
        pic1 = pickle.dump(value)
        unpickle = pickle.load(pic1)
        pic2 = pickle.dump(unpickle)
    
    assert(pic1 == pic2)

def generate_tuple():
    """
    Generate a random tuple of values
    """
    tuple = ()
    for _ in range(random.randint(1, 1000)):
        tuple += (random.randint(1, 1000),)
    return tuple


def generate_list():
    """
    Generate a random list of values
    """
    list = []
    for _ in range(random.randint(1, 1000)):
        list.append(random.randint(1, 1000))
    return list

def generate_dict():
    """
    Generate a random dict of values
    """
    dict = {}
    for _ in range(random.randint(1, 1000)):
        dict[random.randint(1, 1000)] = random.randint(1, 1000)
    return dict

def random_data_generator():
    """
    Generate a random tuple of values
    """
    while True:
        yield generate_tuple()

def main():
    random.seed(9001)
    data_generator = random_data_generator()
    for _ in tqdm(range(1000)):
        data = next(data_generator)
        test1(data)
        test2(data)

if __name__ == "__main__":
    main()

