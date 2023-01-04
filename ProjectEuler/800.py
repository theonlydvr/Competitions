import math

import lib

primes = lib.file_to_ints('../primes.txt') + lib.file_to_ints('../primes2.txt')
primes = [i for l in primes for i in l]
logp = [math.log10(p) for p in primes]
lim = 800800*math.log10(800800)
count = 0
highest = -1
while primes[highest] * logp[0] + primes[0] * logp[highest] > lim:
    highest -= 1
for i in range(len(primes)):
    while highest > -(len(primes)-i) and primes[highest] * logp[i] + primes[i] * logp[highest] > lim:
        highest -= 1
    if highest <= -(len(primes)-i):
        break
    count += (len(primes)+highest) - i
print(count)
