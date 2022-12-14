# P1
cave = [[0]]
lmost = 500
bmost = 0
with open('input.txt', 'r') as f:
    for line in f:
        commands = line[:-1].split(' -> ')
        for i in range(len(commands) - 1):
            parts1 = commands[i].split(',')
            parts1 = (int(parts1[0]), int(parts1[1]))
            parts2 = commands[i+1].split(',')
            parts2 = (int(parts2[0]), int(parts2[1]))
            if parts1[0] != parts2[0]:
                step = 0
            else:
                step = 1
            if parts1[step] > parts2[step]:
                steps = range(parts1[step], parts2[step]-1, -1)
            else:
                steps = range(parts1[step], parts2[step]+1, 1)
            for v in steps:
                if step == 0:
                    comp = (v, parts1[1])
                else:
                    comp = (parts1[0], v)
                while comp[0] - lmost < 0:
                    for row in cave:
                        row.insert(0, 0)
                    lmost -= 1
                while comp[0] - lmost >= len(cave[0]):
                    for row in cave:
                        row.append(0)
                while bmost - comp[1] < 0:
                    cave.append([0]*len(cave[0]))
                    bmost += 1
                cave[comp[1]][comp[0] - lmost] = 1

count = 0
pos = (500, 0)
while True:
    if pos[1] + 1 == len(cave):
        break
    elif cave[pos[1]+1][pos[0]-lmost] == 0:
        pos = (pos[0], pos[1]+1)
    else:
        if pos[0] - 1 < lmost:
            break
        elif cave[pos[1]+1][pos[0]-1-lmost] == 0:
            pos = (pos[0]-1, pos[1]+1)
        else:
            if pos[0] - lmost >= len(cave[0]):
                break
            elif cave[pos[1]+1][pos[0]+1-lmost] == 0:
                pos = (pos[0]+1, pos[1]+1)
            else:
                cave[pos[1]][pos[0]-lmost] = 1
                pos = (500, 0)
                count += 1

print(count)

# P2

cave = [[0]]
lmost = 500
bmost = 0
with open('input.txt', 'r') as f:
    for line in f:
        commands = line[:-1].split(' -> ')
        for i in range(len(commands) - 1):
            parts1 = commands[i].split(',')
            parts1 = (int(parts1[0]), int(parts1[1]))
            parts2 = commands[i+1].split(',')
            parts2 = (int(parts2[0]), int(parts2[1]))
            if parts1[0] != parts2[0]:
                step = 0
            else:
                step = 1
            if parts1[step] > parts2[step]:
                steps = range(parts1[step], parts2[step]-1, -1)
            else:
                steps = range(parts1[step], parts2[step]+1, 1)
            for v in steps:
                if step == 0:
                    comp = (v, parts1[1])
                else:
                    comp = (parts1[0], v)
                while comp[0] - lmost < 0:
                    for row in cave:
                        row.insert(0, 0)
                    lmost -= 1
                while comp[0] - lmost >= len(cave[0]):
                    for row in cave:
                        row.append(0)
                while bmost - comp[1] < 0:
                    cave.append([0]*len(cave[0]))
                    bmost += 1
                cave[comp[1]][comp[0] - lmost] = 1

cave.append([0]*len(cave[0]))
cave.append([1]*len(cave[0]))
count = 1
pos = (500, 0)
while True:
    if cave[pos[1]+1][pos[0]-lmost] == 0:
        pos = (pos[0], pos[1]+1)
    else:
        if pos[0] - 1 < lmost:
            for row in cave:
                row.insert(0, 0)
            lmost -= 1
            cave[-1][0] = 1
            cave[-2][1] = 1
            pos = (500, 0)
            count += 1
        elif cave[pos[1]+1][pos[0]-1-lmost] == 0:
            pos = (pos[0]-1, pos[1]+1)
        else:
            if pos[0] + 1 - lmost == len(cave[0]):
                for row in cave:
                    row.append(0)
                cave[-1][-1] = 1
                cave[-2][-2] = 1
                pos = (500, 0)
                count += 1
            elif cave[pos[1]+1][pos[0]+1-lmost] == 0:
                pos = (pos[0]+1, pos[1]+1)
            else:
                if pos == (500, 0):
                    break
                else:
                    cave[pos[1]][pos[0]-lmost] = 1
                    pos = (500, 0)
                    count += 1

print(count)