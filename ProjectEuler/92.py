en = {89}
one = {1}
count = 0
for i in range(1, 10**7):
    if i in en:
        count += 1
    elif i not in one:
        seq = [i]
        nxt = sum([int(c)**2 for c in str(seq[-1])])
        while nxt not in en and nxt not in one:
            seq.append(nxt)
            nxt = sum([int(c) ** 2 for c in str(seq[-1])])
        if nxt in en:
            for n in seq:
                en.add(n)
            count += 1
        elif nxt in one:
            for n in seq:
                one.add(n)

print(count)
