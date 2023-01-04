import sys

import lib


def check_combos(pg, group):
    if len(group) == N:
        return sum(group)
    elif len(pg) == 0:
        return None
    else:
        comb = check_combos(pg[1:], group)  # skip
        if comb is None:
            vld = True
            for p in group:
                if frozenset([pg[0], p]) not in pos_com:
                    vld = False
            if vld:
                grp = group.copy()
                grp.add(pg[0])
                comb = check_combos(pg[1:], grp)
        return comb


sys.setrecursionlimit(2000)
pos_com = set()
primes = lib.file_to_ints('../primes.txt') + lib.file_to_ints('../primes2.txt')
primes = [i for l in primes for i in l]
pset = set(primes)
valid = True
N = 5

for i in range(2, len(primes)):
    for j in range(i):
        if int(str(primes[i]) + str(primes[j])) in pset and int(str(primes[j]) + str(primes[i])) in pset:
            pos_com.add(frozenset([primes[i], primes[j]]))
        elif lib.is_prime(int(str(primes[i]) + str(primes[j]))) and lib.is_prime(int(str(primes[j]) + str(primes[i]))):
            pset.add(int(str(primes[i]) + str(primes[j])))
            pset.add(int(str(primes[j]) + str(primes[i])))
            pos_com.add(frozenset([primes[i], primes[j]]))
    if i >= N:
        check = check_combos(primes[:i-1], {primes[i]})
        if check is not None:
            print(check)
            break
