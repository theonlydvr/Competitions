import lib

primes = set()
for i in range(2, 1000000):
    if i not in primes and lib.is_prime(i):
        p = str(i)
        valid = True
        for j in range(len(p)):
            if int(p) not in primes:
                if not lib.is_prime(int(p)):
                    valid = False
                    break
            p = p[1:] + p[0]

        if valid:
            for j in range(len(p)):
                primes.add(int(p))
                p = p[1:] + p[0]
print(primes)

print(len(primes))
