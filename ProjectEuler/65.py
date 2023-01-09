from fractions import Fraction

seq = [2, 1]
N = 100

k = 1
while len(seq) < N:
    seq += [2 * k, 1, 1]
    k += 1

seq = seq[:N]

frac = Fraction(seq[-1], 1)

for i in range(-2, -N - 1, -1):
    frac = seq[i] + Fraction(1, frac)

print(sum([int(n) for n in str(frac.numerator)]))
