from functools import reduce
from operator import getitem

# deep_get({"a": [1, 2, 3]}, ["a", 1]) -> 2
def deep_get(data, keys):
    return reduce(getitem, keys, data)
