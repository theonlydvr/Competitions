pans = 0
panset = set()

for i in range(1, 10000):
    si = str(i)
    for j in range(i+1, 10000):
        sj = str(j)
        res = str(i * j)
        comb = si + sj + res
        if len(comb) > 9:
            break
        elif '0' not in comb and len(set(comb)) == 9:
            if i * j not in panset:
                pans += i * j
                panset.add(i * j)

print(pans)
