abundant = []
for i in range(1, 28123):
    divisors = set()
    for j in range(1, round(i ** (1 / 2)) + 1):
        if i % j == 0:
            divisors.add(j)
            divisors.add(i / j)
    if sum(divisors) - i > i:
        abundant.append(i)
ab_set = set(abundant)
no_sum = 0
for i in range(1, 28124):
    j = 0
    found = False
    while j < len(abundant) and abundant[j] < i:
        if i - abundant[j] in ab_set:
            found = True
            break
        j += 1
    if not found:
        no_sum += i

print(no_sum)
