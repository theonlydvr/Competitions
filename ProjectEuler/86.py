from decimal import Decimal

M = 0
n_sol = 0

while True:
    M += 1
    for i in range(2, 2 * M + 1):
        if Decimal(M ** 2 + i ** 2).sqrt() % 1 == 0:
            n_sol += min(M + 1 - -(i // -2), i // 2)
    if n_sol > 10 ** 6:
        break

print(M)
