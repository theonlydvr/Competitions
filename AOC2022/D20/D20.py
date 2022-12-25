# P1
order = []
indices = {}
values = {}
ind = 0
zk = None
with open('input.txt', 'r') as f:
    for line in f:
        if int(line[:-1]) == 0:
            zk = (int(line[:-1]),ind)
        order.append((int(line[:-1]),ind))
        indices[(int(line[:-1]),ind)] = ind 
        values[ind] = (int(line[:-1]),ind)
        ind += 1
    
for i in range(len(order)):
    if order[i % len(order)][0] >= 0:
        shift = order[i][0] % (len(order)-1)
    else:
        shift = order[i][0] % -(len(order)-1)
    start = indices[order[i]]
    if shift > 0:
        step = 1
    else:
        step = -1
    shifted = order[i]
    j = 0
    while j != shift:
        temp = values[(start+j+step)%len(order)]
        indices[temp] =(start+j)%len(order)
        values[(start+j)%len(order)] = temp
        j += step
    indices[shifted] = (start+shift)%len(order)
    values[(start+shift)%len(order)] = shifted

print(values[(indices[zk]+1000)%len(order)][0]+values[(indices[zk]+2000)%len(order)][0]+values[(indices[zk]+3000)%len(order)][0])

# P2
order = []
indices = {}
values = {}
ind = 0
zk = None
key = 811589153
with open('input.txt', 'r') as f:
    for line in f:
        if int(line[:-1]) == 0:
            zk = (int(line[:-1]),ind)
        order.append((int(line[:-1])*key,ind))
        indices[(int(line[:-1])*key,ind)] = ind 
        values[ind] = (int(line[:-1])*key,ind)
        ind += 1
    
for i in range(len(order)*10):
    if order[i % len(order)][0] >= 0:
        shift = order[i % len(order)][0] % (len(order)-1)
    else:
        shift = order[i % len(order)][0] % -(len(order)-1)
    start = indices[order[i % len(order)]]
    if shift > 0:
        step = 1
    else:
        step = -1
    shifted = order[i%len(order)]
    j = 0
    while j != shift:
        temp = values[(start+j+step)%len(order)]
        indices[temp] =(start+j)%len(order)
        values[(start+j)%len(order)] = temp
        j += step
    indices[shifted] = (start+shift)%len(order)
    values[(start+shift)%len(order)] = shifted

print(values[(indices[zk]+1000)%len(order)][0]+values[(indices[zk]+2000)%len(order)][0]+values[(indices[zk]+3000)%len(order)][0])
