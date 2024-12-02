import lib

# P1
lines = lib.split_file('input.txt')
l0 = [int(line[0]) for line in lines]
l1 = [int(line[-1]) for line in lines]
l0.sort()
l1.sort()
print(sum(abs(i - j) for (i, j) in zip(l0, l1)))

# P2
s = set(l0)
d = {}
for l in l1:
    if l in d:
        d[l] += 1
    else:
        d[l] = 1
print(sum(d[l] * l if l in d else 0 for l in s))