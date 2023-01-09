import lib
import networkx

data = lib.file_to_ints('p082_matrix.txt')
G = networkx.DiGraph()

for i in range(len(data)):
    for j in range(len(data[0])):
        if i + 1 < len(data):
            G.add_edge((i, j), (i+1, j), weight=data[i+1][j])
        if i - 1 >= 0:
            G.add_edge((i, j), (i-1, j), weight=data[i-1][j])
        if j + 1 < len(data[0]):
            G.add_edge((i, j), (i, j+1), weight=data[i][j+1])

unvisited = {}
for node in G.nodes:
    if node[1] == 0:
        unvisited[node] = data[node[0]][0]
    else:
        unvisited[node] = float('inf')

while True:
    cur_min = min(unvisited, key=unvisited.get)
    if cur_min[1] == 79:
        break
    neighbors = G[cur_min]
    for n in neighbors:
        if n in unvisited:
            unvisited[n] = min(unvisited[n], unvisited[cur_min] + G[cur_min][n]['weight'])
    del unvisited[cur_min]

print(unvisited[cur_min])
