import pickle

def test1():
    value = 1
    pickle1 = pickle.dumps(value)
    unpickle = pickle.loads(pickle1)
    assert(value == unpickle)

def test2():
    value = 1
    pickle1 = pickle.dumps(value)
    unpickle = pickle.loads(pickle1)
    pickle2 = pickle.dumps(unpickle)
    assert(pickle1 == pickle2)

