P = [1, 1, 2, 3, 5, 7]

while P[-1] != 0:
    Pn = 0
    k = 1
    n = len(P)
    while n - k * (3 * k - 1) / 2 >= 0:
        Pn += (-1) ** (k + 1) * P[n - int(k * (3 * k - 1) / 2)] % 10 ** 6
        k += 1
    k = -1
    while len(P) - k * (3 * k - 1) / 2 >= 0:
        Pn += (-1) ** (k + 1) * P[n - int(k * (3 * k - 1) / 2)] % 10 ** 6
        k -= 1
    P.append(int(Pn) % 10 ** 6)
print(len(P) - 1)