# P1
heightmap = []
row = -1
start = (0, 0)
end = (0, 0)
unvisited = set(())
distances = {}
with open('input.txt', 'r') as f:
    for line in f:
        row += 1
        heightmap.append([])
        for c in range(len(line)-1):
            if line[c] == 'S':
                start = (row, c)
                heightmap[row].append(ord('a'))
            elif line[c] == 'E':
                end = (row, c)
                heightmap[row].append(ord('z'))
            else:
                heightmap[row].append(ord(line[c]))
            unvisited.add((row, c))
            distances[(row, c)] = float('inf')

distances[start] = 0
steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

cur_node = start

while cur_node != end:
    for step in steps:
        r = cur_node[0] + step[0]
        c = cur_node[1] + step[1]
        if (r, c) in unvisited:
            if heightmap[r][c] - heightmap[cur_node[0]][cur_node[1]] <= 1 and distances[(r, c)] > distances[cur_node] + 1:
                distances[(r, c)] = distances[cur_node] + 1
    unvisited.remove(cur_node)
    min_distance = float('inf')
    for node in unvisited:
        if distances[node] < min_distance:
            min_distance = distances[node]
            cur_node = node

print(distances[end])

# P2
heightmap = []
row = -1
start = (0, 0)
end = (0, 0)
unvisited = set(())
distances = {}
with open('input.txt', 'r') as f:
    for line in f:
        row += 1
        heightmap.append([])
        for c in range(len(line)-1):
            if line[c] == 'S':
                start = (row, c)
                heightmap[row].append(ord('a'))
            elif line[c] == 'E':
                end = (row, c)
                heightmap[row].append(ord('z'))
            else:
                heightmap[row].append(ord(line[c]))
            unvisited.add((row, c))
            distances[(row, c)] = float('inf')

distances[end] = 0
steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]

cur_node = end

while heightmap[cur_node[0]][cur_node[1]] != ord('a'):
    for step in steps:
        r = cur_node[0] + step[0]
        c = cur_node[1] + step[1]
        if (r, c) in unvisited:
            if heightmap[cur_node[0]][cur_node[1]] - heightmap[r][c] <= 1 and distances[(r, c)] > distances[cur_node] + 1:
                distances[(r, c)] = distances[cur_node] + 1
    unvisited.remove(cur_node)
    min_distance = float('inf')
    for node in unvisited:
        if distances[node] < min_distance:
            min_distance = distances[node]
            cur_node = node

print(distances[cur_node])