from decimal import Decimal

import lib

primes = lib.file_to_ints('../primes.txt') + lib.file_to_ints('../primes2.txt')
primes = [i for l in primes for i in l]
primes.sort()
pset = set(primes)
count = 0
all_sum = 0
i = 2
while count < 50:
    sq = str(primes[i] ** 2)
    sq2 = sq[::-1]
    if sq != sq2:
        root = Decimal(int(sq2)).sqrt()
        if root % 1 == 0 and int(root) in pset:
            all_sum += primes[i] ** 2
            count += 1
    i += 1

print(all_sum)
