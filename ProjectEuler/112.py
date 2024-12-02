from fractions import Fraction

bouncy = 0
n = 1
target = Fraction(99, 100)

while Fraction(bouncy, n) != target:
    n += 1
    bouncy += not all([n // 10 ** i % 10 <= n // 10 ** (i + 1) % 10 for i in range(len(str(n)) - 1)]) and not all(
        [n // 10 ** i % 10 >= n // 10 ** (i + 1) % 10 for i in range(len(str(n)) - 1)])

print(n)
