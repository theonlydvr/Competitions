import more_itertools as mit
from sympy.utilities.iterables import multiset_permutations

import lib
import math


def all_unique_splits(lst):
    combined = set()
    perms = multiset_permutations(lst)
    for perm in perms:
        splits = list(mit.partitions(list(perm)))
        for split in splits:
            sorted = [math.prod(l) for l in split]
            sorted.sort()
            combined.add(tuple(sorted))
    return [list(x) for x in combined]


min_set = set()
num = 2
factor_dict = dict.fromkeys((range(2, 20000)))

for k in range(2, 12000):
    valid = False
    while not valid:
        if num in factor_dict and factor_dict[num] is not None:
            splits = factor_dict[num]
        else:
            factors = lib.prime_factorize(num)
            splits = all_unique_splits(factors)
            factor_dict[num] = splits
        for split in splits:
            if len(split) <= k:
                if sum(split) + k - len(split) == num:
                    valid = True
                    break
        if valid:
            break
        num += 1
    min_set.add(num)
    num = k

print(sum(min_set))
