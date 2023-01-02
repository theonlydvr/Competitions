import sys
from fractions import Fraction


def continued_frac(target, n):
    if n == target:
        return 0
    else:
        return Fraction(1 / (2 + continued_frac(target, n + 1)))


sys.setrecursionlimit(1500)
count = 0

for i in range(1, 1001):
    frac = 1 + continued_frac(i, 0)
    if len(str(frac.numerator)) > len(str(frac.denominator)):
        count += 1

print(count)
