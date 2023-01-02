import math

all_sum = 0
for j in range(10, 100000):
    fac_sum = 0
    for c in str(j):
        fac_sum += math.factorial(int(c))
    if fac_sum == j:
        all_sum += j

print(all_sum)