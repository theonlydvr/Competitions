import lib
from itertools import permutations

full = '123456789'
largest = 0
for i in range(2, len(full) + 1):
    perms = set([''.join(p) for p in permutations(full[:i+1])])
    for p in perms:
        if lib.is_prime(int(p)):
            largest = max(largest, int(p))

print(largest)