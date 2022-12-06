#P1
counter = 0
with open('input.txt', 'r') as f:
    for line in f:
        r0 = line[0:int((len(line)-1)/2)]
        r1 = line[int((len(line)-1)/2):len(line)-1]
        p = ord([v for v in r0 if v in r1][0])
        if p >= 97:
            p -= 96
        else:
            p -= 38
        counter += p

print(counter)

#P2
counter = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        p = ord([v for v in lines[i] if v in lines[i+1] and v in lines[i+2]][0])
        if p >= 97:
            p -= 96
        else:
            p -= 38
        counter += p

print(counter)