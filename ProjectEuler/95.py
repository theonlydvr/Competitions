import lib

divisor_sums = {}
max_cycle = 0
min_chain = 0

for i in range(1, 10**6+1):
    num = i
    cycle = 0
    minN = num
    seen = set()
    while num <= 10 ** 6 and num not in seen:
        if num in divisor_sums:
            divisor_sum = divisor_sums[num]
        else:
            divisors = list(lib.divisors(num))
            divisors.remove(num)
            divisor_sum = sum(divisors)
        if divisor_sum > 1:
            seen.add(num)
            num = divisor_sum
            minN = min(minN, num)
            cycle += 1
        else:
            divisor_sums[num] = 1
            break

    if num == i and cycle > max_cycle:
        max_cycle = cycle
        min_chain = minN

print(min_chain)
