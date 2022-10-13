def get_none():
    return None

def flatten_dict(dict):
    x = list(dict.values())
    print(x)
    return x


flatten_dict({'a': 42, 'b': 3.14})
flatten_dict({'a': [42, 350], 'b': 3.14})