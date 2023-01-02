all_sum = 0
for i in range (1, 1000001):
    si = str(i)
    valid = True
    for j in range(int(len(si)/2)):
        if si[j] != si[-(j + 1)]:
            valid = False
            break
    if valid:
        si = str(bin(i))[2:]
        for j in range(int(len(si) / 2)):
            if si[j] != si[-(j + 1)]:
                valid = False
                break
        if valid:
            all_sum += i

print(all_sum)