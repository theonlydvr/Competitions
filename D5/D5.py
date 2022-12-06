#P1
stacks=[[] for i in range(9)]
with open('input.txt', 'r') as f:
    for line in f:
        if line[0] == 'm':
            commands = line.split(' ')
            m = int(commands[1])
            fr = int(commands[3])
            t = int(commands[5])
            for i in range(m):
                stacks[t-1].append(stacks[fr-1].pop())
        elif line.__contains__('['):
            for i in range(9):
                if line[i*4+1] != ' ':
                    stacks[i].insert(0, line[i*4+1])
                    
msg = ""
for s in stacks:
    msg += s[-1]
print(msg)

#P2
stacks=[[] for i in range(9)]
with open('input.txt', 'r') as f:
    for line in f:
        if line[0] == 'm':
            commands = line.split(' ')
            m = int(commands[1])
            fr = int(commands[3])
            t = int(commands[5])
            moved = stacks[fr-1][-m:]
            stacks[t-1] = stacks[t-1] + moved
            stacks[fr-1] = stacks[fr-1][:-m]
        elif line.__contains__('['):
            for i in range(9):
                if line[i*4+1] != ' ':
                    stacks[i].insert(0, line[i*4+1])
                    
msg = ""
for s in stacks:
    msg += s[-1]
print(msg)