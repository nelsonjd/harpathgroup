import itertools

def flatten(list2d: list) -> list:
    return list(itertools.chain.from_iterable(list2d))