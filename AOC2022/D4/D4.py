#P1
counter = 0
with open('input.txt', 'r') as f:
    for line in f:
        x=line.split(',')
        e1=x[0].split('-')
        e1 = [int(i) for i in e1]
        e2=x[1].split('-')
        e2 = [int(i) for i in e2]
        if (e1[0] <= e2[0] and e1[1] >= e2[1]) or (e2[0] <= e1[0] and e2[1] >= e1[1]):
            counter += 1

print(counter)

#P2
counter = 0
with open('input.txt', 'r') as f:
    for line in f:
        x=line.split(',')
        e1=x[0].split('-')
        e1 = [int(i) for i in e1]
        e2=x[1].split('-')
        e2 = [int(i) for i in e2]
        if (e1[0] >= e2[0] and e1[0] <= e2[1]) or (e2[0] >= e1[0] and e2[0] <= e1[1]):
            counter += 1
        elif (e1[1] >= e2[0] and e1[1] <= e2[1]) or (e2[1] >= e1[1] and e2[1] <= e1[1]):
            counter += 1

print(counter)