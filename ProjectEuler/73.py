import math
from fractions import Fraction

ref1 = Fraction(1, 3)
ref2 = Fraction(1, 2)
frac_set = set()

for d in range(3, 12001):
    n0 = math.ceil(d / 3)
    n1 = math.floor(d / 2)
    for n in range(n0, n1 + 1):
        frac_set.add(Fraction(n, d))

print(len(frac_set) - 2)
