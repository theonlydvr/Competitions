cals = []
counter = 0
with open('input.txt', 'r') as f:
    for line in f:
        if line == '\n':
            cals.append(counter)
            counter = 0
        else:
            counter += int(line)
cals.sort(reverse=True)
# P1
print(cals[0])
# P2
print(cals[0]+cals[1]+cals[2])