import lib

longest = 0
prod = 0

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        ind = 0
        while lib.is_prime(abs(ind ** 2 + a * ind + b)):
            ind += 1
        if ind > longest:
            longest = ind
            prod = a * b

print(prod)
