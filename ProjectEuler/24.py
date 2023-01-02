numbers = list(range(10))

place = 2
used = [1] * (len(numbers)-1)
for i in range(1000000-1):
    seg = numbers[-place:]
    seg.sort()
    ins = seg[used[-(place - 1)]]
    seg.remove(ins)
    numbers = numbers[:-place] + [ins] + seg
    used[-(place - 1)] += 1
    if used[-(place - 1)] == place:
        j = -1
        place = 2
        while used[j] == place:
            place += 1
            j -= 1
        for j in range(-place + 2, 0):
            used[j] = 1
    else:
        place = 2

print(''.join([str(n) for n in numbers]))
