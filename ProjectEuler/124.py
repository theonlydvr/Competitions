import operator
import bisect
from functools import reduce

import lib

rads = []
radinds = {}
for i in range(1, 100001):
    vals = lib.prime_factorize(i)
    rad = reduce(operator.mul, set(vals), 1)
    if len(rads) < 10000:
        bisect.insort(rads, (rad, i))
    elif rad < rads[-1][0]:
        bisect.insort(rads, (rad, i))
        del rads[-1]
print(rads[-1])
