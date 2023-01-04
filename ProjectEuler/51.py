import itertools

import lib

primes = lib.file_to_ints('../primes.txt') + lib.file_to_ints('../primes2.txt')
primes = [i for l in primes for i in l]
pset = set(primes)

for p in primes:
    ps = set()
    if p > 56003:
        sp = str(p)
        inds = set(range(len(sp)))
        for i in range(1, len(sp)):
            subs = list(itertools.combinations(inds, i))
            for s in subs:
                for j in range(10):
                    st = sp
                    for c in s:
                        st = st[:c] + str(j) + st[c+1:]
                    if len(str(int(st))) == len(sp) and int(st) in pset:
                        ps.add(int(st))
                if len(ps) >= 8:
                    break
                ps = set()
            if len(ps) >= 8:
                break
    if len(ps) >= 8:
        print(min(ps))
        break
