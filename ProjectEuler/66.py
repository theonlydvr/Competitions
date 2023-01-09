import math
from decimal import *
from fractions import Fraction

getcontext().prec = 1000
largest_min = 0
D_for_min = 0
for D in range(2, 1001):
    if Decimal(D).sqrt() % 1 != 0:
        cur = Decimal(D).sqrt()
        seq = [math.floor(cur)]
        sol = Fraction(seq[0], 1)
        while sol.numerator ** 2 - D * sol.denominator ** 2 != 1:
            cur = Decimal(1) / (cur - seq[-1])
            seq.append(math.floor(cur))
            sol = Fraction(seq[-1])
            for i in range(-2, -len(seq) - 1, -1):
                sol = Fraction(seq[i]) + Fraction(sol.denominator, sol.numerator)
        if sol.numerator > largest_min:
            largest_min = sol.numerator
            D_for_min = D

print(D_for_min)
