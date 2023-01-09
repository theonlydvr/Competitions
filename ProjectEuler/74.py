import math

seen = set()
chain60 = 0

for i in range(10 ** 6 + 1):
    if i not in seen:
        seq = []
        seq_set = set()
        cur = i
        while cur not in seq_set:
            seq.append(cur)
            seq_set.add(cur)
            seen.add(cur)
            cur = sum([math.factorial(int(n)) for n in str(cur)])
        if len(seq) == 60:
            chain60 += 1

print(chain60)
