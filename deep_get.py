from functools import reduce
from operator import getitem

def deep_get(collection, iterable):
    return reduce(getitem, iterable, collection)
