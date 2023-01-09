import itertools

import lib

data = lib.file_to_ints('../primes.txt')
data = [item for sub in data for item in sub]

sums = set()
prime_bag = []
i = 0
while data[i] ** 2 + 2 ** 3 + 2 ** 4 < 50 * 10 ** 6:
    if data[i] ** 2 + data[i] ** 3 + 2 ** 4 < 50 * 10 ** 6:
        prime_bag.append(data[i])
    if data[i] ** 2 + data[i] ** 3 + data[i] ** 4 < 50 * 10 ** 6:
        prime_bag.append(data[i])
    combs = set(itertools.combinations(prime_bag, 2))
    for c in combs:
        if data[i] ** 2 + c[0] ** 3 + c[1] ** 4 < 50 * 10 ** 6:
            sums.add(data[i] ** 2 + c[0] ** 3 + c[1] ** 4)
        if data[i] ** 2 + c[1] ** 3 + c[0] ** 4 < 50 * 10 ** 6:
            sums.add(data[i] ** 2 + c[1] ** 3 + c[0] ** 4)
        if data[i] ** 3 + c[1] ** 2 + c[0] ** 4 < 50 * 10 ** 6:
            sums.add(data[i] ** 3 + c[1] ** 2 + c[0] ** 4)
        if data[i] ** 4 + c[1] ** 2 + c[0] ** 3 < 50 * 10 ** 6:
            sums.add(data[i] ** 4 + c[1] ** 2 + c[0] ** 3)
        if data[i] ** 3 + c[0] ** 2 + c[1] ** 4 < 50 * 10 ** 6:
            sums.add(data[i] ** 3 + c[0] ** 2 + c[1] ** 4)
        if data[i] ** 4 + c[0] ** 2 + c[1] ** 3 < 50 * 10 ** 6:
            sums.add(data[i] ** 4 + c[0] ** 2 + c[1] ** 3)
    i += 1

print(len(sums))
