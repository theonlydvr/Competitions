from sympy import divisors

n = 10 * 10 ** 6
mx = 0
while len(divisors(n)) - 1 < 1000:
    if len(divisors(n)) - 1 > mx:
        mx = len(divisors(n)) - 1
        print(str(mx) + ' ' + str(n))
    n += 1

print(n)
