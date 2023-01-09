import math

m = 2

perims = {}

while True:
    k = 1
    while True:
        count = 0
        for n in range(1, m):
            if not (n % 2 == 1 and m % 2 == 1) and math.gcd(n, m) == 1:
                a = k * (m ** 2 - n ** 2)
                b = 2 * k * m * n
                c = k * (m ** 2 + n ** 2)
                if a + b + c > 1.5 * 10 ** 6:
                    count += 1
                else:
                    if a + b + c in perims:
                        perims[a + b + c] += 1
                    else:
                        perims[a + b + c] = 1
            else:
                count += 1
        if count == m - 1:
            break
        k += 1
    if k == 1 and count == m - 1:
        break
    m += 1

print(sum([v == 1 for v in perims.values()]))
