from itertools import permutations

all_sum = 0
base = '0123456789'
order = [2, 3, 5, 7, 11, 13, 17]
perms = set([''.join(p) for p in permutations(base)])
for p in perms:
    if not p.startswith('0'):
        valid = True
        for i in range(1, 8):
            if int(p[i:i+3]) % order[i-1] != 0:
                valid = False
        if valid:
            all_sum += int(p)

print(all_sum)
