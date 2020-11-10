import pickle

data = {
    'a': [1,2,3,4],
    'b': ("Uno", "Dos"),
    'c': True,
    'd': "una cadena"
}

pickled_data = pickle.dumps(data)

unpickled_data = pickle.loads(pickled_data)

print(unpickled_data)