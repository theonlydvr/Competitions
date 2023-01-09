import lib


def make_sums(num, primes, cur):
    if num == 0:
        return 1
    elif num < 0:
        return 0
    else:
        total = 0
        for p in primes:
            if p <= cur:
                total += make_sums(num - p, primes, p)
        return total


data = lib.file_to_ints('../primes.txt')
data = [item for sub in data for item in sub]

num = 2

while True:
    primes = []
    for p in data:
        if p <= num:
            primes.append(p)
        if p >= num:
            break
    check = make_sums(num, primes, primes[-1])
    if check > 5000:
        print(num)
        break
    num += 1
