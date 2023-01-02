import lib
import networkx as nx

data = lib.file_to_ints('67.txt')
G = nx.Graph()
G.add_node((0, 0))
root = (0, 0)
nodes = {root: data[0][0]}
for i in range(1, len(data)):
    new_nodes = []
    G.add_node((i, 0))
    nodes[(i, 0)] = 0
    for j in range(len(data[i])-1):
        G.add_node((i, j + 1))
        nodes[(i, j + 1)] = 0
        G.add_edge((i-1, j), (i, j))
        G.add_edge((i-1, j), (i, j + 1))

visited = []
for i in range(len(data) - 1):
    for j in range(len(data[i])):
        children = list(G.adj[(i, j)].keys())
        nodes[children[-2]] = max(nodes[children[-2]], nodes[(i, j)] + data[children[-2][0]][children[-2][1]])
        nodes[children[-1]] = max(nodes[children[-1]], nodes[(i, j)] + data[children[-1][0]][children[-1][1]])

max_path = 0
for i in range(len(data[-1])):
    max_path = max(max_path, nodes[(len(data)-1, i)])

print(max_path)
