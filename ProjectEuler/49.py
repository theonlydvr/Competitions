import lib
from itertools import permutations, combinations

primes = []
for i in range(1001, 10000):
    if lib.is_prime(i):
        primes.append(i)

for p in primes:
    perms = set([''.join(p) for p in permutations(str(p))])
    seq = set()
    for per in perms:
        if not per.startswith('0'):
            if lib.is_prime(int(per)):
                seq.add((int(per)))
    if len(seq) >= 3:
        combs = list(combinations(seq, 3))
        found = False
        for comb in combs:
            comb2 = list(comb)
            comb2.sort()
            if comb[0] != 1487 and comb2[1] - comb2[0] == comb2[2] - comb2[1]:
                print(str(comb2[0])+str(comb2[1])+str(comb2[2]))
                found = True
                break
        if found:
            break
