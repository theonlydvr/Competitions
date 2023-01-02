max_sum = 0

for a in range(100):
    for b in range(100):
        max_sum = max(max_sum, sum([int(c) for c in str(a ** b)]))

print(max_sum)