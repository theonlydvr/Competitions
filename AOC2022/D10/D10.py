import math
#P1
X = 1
cycle = 1
interest = 20
total = 0

with open('input.txt', 'r') as f:
    for line in f:
        if line.startswith('noop'):
            cycle += 1
        else:
            cycle += 1
            if cycle == interest:
                total += cycle * X
                interest += 40
            X += int(line[:-1].split(' ')[1])
            cycle += 1
        if cycle == interest:
                total += cycle * X
                interest += 40
print(total)

#P2
X = 0
cycle = -1
command = [[]]

with open('input.txt', 'r') as f:
    for line in f:
        if line.startswith('noop'):
            cycle += 1
        else:
            cycle += 1
            if math.floor(cycle/40) >= len(command):
                command.append([])
            if abs(X-(cycle % 40)) <= 1:
                command[math.floor(cycle/40)].append('#')
            else:
                command[math.floor(cycle/40)].append('.')
            X += int(line[:-1].split(' ')[1])
            cycle += 1
        if math.floor(cycle/40) >= len(command):
            command.append([])
        if abs(X-(cycle % 40)) <= 1:
            command[math.floor(cycle/40)].append('#')
        else:
            command[math.floor(cycle/40)].append('.')
for c in command:
    print(c)