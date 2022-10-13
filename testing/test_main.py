from main import *

def test_get_none():
    assert get_none() == None

def test_flatten_dict():
    assert flatten_dict({"a": 2}) == [2]
    assert flatten_dict({"a": "sadd", "b": 4}) == ["sadd", 4]
    assert flatten_dict({'a': [42, 350], 'b': 3.14}) == [[42, 350], 3.14]
