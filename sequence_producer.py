import typing
from itertools import permutations, combinations

def sequence_producer(sequence_len: int, groups: typing.Dict[typing.Hashable, int]) -> typing.Iterator[typing.List[int]]:
    """Yields all possible sequences of the given length, with the given groups appearing the given number of times.

    Args:
        len: The length of the sequence
        groups: A dict of the groups and the number of times they should appear in the sequence
    """
    outputs = []
    values = []
    for group, count in groups.items():
        values += [group] * count
    if len(values) < sequence_len:
        values += [None] * (sequence_len - len(values))
    for perm in permutations(values, sequence_len):
        if perm not in outputs:
            outputs.append(perm)
            yield list(perm)
        
