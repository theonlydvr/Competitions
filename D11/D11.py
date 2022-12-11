import math
import primefac

# P1
m = -1
items = []
operations = []
tests = []
trues = []
falses = []

with open('input.txt', 'r') as f:
    for line in f:
        if line.startswith('Monkey'):
            m += 1
        elif line.startswith('  Starting'):
            segs = line[:-1].split(': ')
            m_items = [eval(i) for i in segs[1].split(', ')]
            m_items.reverse()
            items.append(m_items)
        elif line.startswith('  Operation'):
            segs = line[:-1].split(' = ')
            operations.append(segs[1])
        elif line.startswith('  Test'):
            segs = line[:-1].split(' ')
            tests.append(int(segs[-1]))
        elif line.startswith('    If true:'):
            segs = line[:-1].split(' ')
            trues.append(int(segs[-1]))
        elif line.startswith('    If false:'):
            segs = line[:-1].split(' ')
            falses.append(int(segs[-1]))

inspections =[0]*len(items)

for i in range(20):
    for j in range(len(items)):
        for k in range(len(items[j])):
            inspections[j] += 1
            item = items[j].pop()
            worry = eval(operations[j].replace('old', str(item)))
            worry = math.floor(worry / 3)
            if worry % tests[j] == 0:
                items[trues[j]].insert(0, worry)
            else:
                items[falses[j]].insert(0, worry)

inspections.sort(reverse=True)
print(inspections[0]*inspections[1])

# P2

m = -1
items = []
operations = []
tests = []
trues = []
falses = []

with open('input.txt', 'r') as f:
    for line in f:
        if line.startswith('Monkey'):
            m += 1
        elif line.startswith('  Starting'):
            segs = line[:-1].split(': ')
            m_items = [eval(i) for i in segs[1].split(', ')]
            m_items.reverse()
            items.append(m_items)
        elif line.startswith('  Operation'):
            segs = line[:-1].split(' = ')
            operations.append(segs[1])
        elif line.startswith('  Test'):
            segs = line[:-1].split(' ')
            tests.append(int(segs[-1]))
        elif line.startswith('    If true:'):
            segs = line[:-1].split(' ')
            trues.append(int(segs[-1]))
        elif line.startswith('    If false:'):
            segs = line[:-1].split(' ')
            falses.append(int(segs[-1]))

inspections =[0]*len(items)
base = 1
for test in tests:
    base *= test

for i in range(10000):
    for j in range(len(items)):
        for k in range(len(items[j])):
            inspections[j] += 1
            item = items[j].pop()
            worry = eval(operations[j].replace('old', str(item))) % base
            if worry % tests[j] == 0:
                items[trues[j]].insert(0, worry)
            else:
                items[falses[j]].insert(0, worry)
    

inspections.sort(reverse=True)
print(inspections[0]*inspections[1])