amicables = []
for i in range(1, 10000):
    if i not in amicables:
        divisors = set()
        for j in range(1, round(i ** (1/2)) + 1):
            if i % j == 0:
                divisors.add(j)
                divisors.add(i/j)
        da = sum(divisors) - i
        divisors2 = set()
        for j in range(1, round(da ** (1/2)) + 1):
            if da % j == 0:
                divisors2.add(j)
                divisors2.add(da/j)
        db = sum(divisors2) - da
        if db == i and da != db:
            amicables.append(da)
            amicables.append(db)

print(amicables)
print(sum(amicables))
