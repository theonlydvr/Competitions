import itertools

combs = list(itertools.combinations(list(range(10)), 6))
valid = set()

for c1 in combs:
    for c2 in combs:
        if ((0 in c1 and 1 in c2) or (0 in c2 and 1 in c1)) and \
           ((0 in c1 and 4 in c2) or (0 in c2 and 4 in c1)) and \
           ((0 in c1 and (6 in c2 or 9 in c2)) or (0 in c2 and (6 in c1 or 9 in c1))) and \
           ((1 in c1 and (6 in c2 or 9 in c2)) or (1 in c2 and (6 in c1 or 9 in c1))) and \
           ((2 in c1 and 5 in c2) or (5 in c1 and 2 in c2)) and \
           ((3 in c1 and (6 in c2 or 9 in c2)) or (3 in c2 and (6 in c1 or 9 in c1))) and \
           ((4 in c1 and (6 in c2 or 9 in c2)) or (4 in c2 and (6 in c1 or 9 in c1))) and \
           ((1 in c1 and 8 in c2) or (8 in c1 and 1 in c2)):
            if c1 + c2 not in valid and c2 + c1 not in valid:
                valid.add(c1 + c2)

print(len(valid))
