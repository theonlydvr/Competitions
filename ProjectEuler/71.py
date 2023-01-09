import math
from fractions import Fraction

ref = Fraction(3, 7)
closest = Fraction(0)

for d in range(1, 10 ** 6 + 1):
    n0 = math.floor(3 / 7 * d)
    for n in range(n0, d - 1):
        f = Fraction(n, d)
        if f >= ref:
            break
        if ref - f < ref - closest:
            closest = f

print(closest)
