import lib

count = 0
i = 2

while count < 4:
    if len(set(lib.prime_factorize(i))) == 4:
        count += 1
    else:
        count = 0
    i += 1

print(i - 4)
