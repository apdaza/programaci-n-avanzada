from pickle import dump, load, HIGHEST_PROTOCOL

data = {
    'a': [1,2,3,4],
    'b': ("Uno", "Dos"),
    'c': True,
    'd': "una cadena"
}

with open('data.pickle', 'wb') as f:
    dump(data, f, protocol=HIGHEST_PROTOCOL)
    f.close()

with open('data.pickle', 'rb') as f:
    data_unpickled = load(f)
    print(data_unpickled)
    print(data_unpickled['a'])
    f.close()