import lib

sum_tot = 0
N = 10 ** 6
for j in range(1, N + 1):
    sum_tot += lib.totient(j)
    if j % 10000 == 0:
        print(j)

print((2 * sum_tot - 1 - 1) / 2)
