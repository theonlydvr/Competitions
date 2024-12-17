import numpy as np
import networkx as nx

import lib

maze = lib.file_to_mat('input.txt')

temp = np.where(maze == 'S')
nodes = [(temp[0][0], temp[1][0], 0, 1)]
maze_graph = nx.Graph()
visited = set()

while len(nodes) > 0:
    new_nodes = set()
    for node in nodes:
        visited.add(node)
        d = (-node[3], node[2])
        cost = -1001
        for i in range(4):
            if maze[node[0] + d[0], node[1] + d[1]] != '#':
                nn = (node[0] + d[0], node[1] + d[1], d[0], d[1])
                if maze_graph.get_edge_data(node, nn) is None:
                    maze_graph.add_edge(node, nn, weight=abs(cost))
                elif maze_graph.get_edge_data(node, nn)['weight'] > abs(cost):
                    maze_graph.get_edge_data(node, nn)['weight'] = abs(cost)
                if nn not in visited:
                    new_nodes.add(nn)
            cost = abs(cost + 1000)
            d = (d[1], -d[0])
    nodes = new_nodes

temp2 = np.where(maze == 'E')
d = (1, 0)
p = []
for i in range(4):
    if (temp2[0][0], temp2[1][0], d[0], d[1]) in maze_graph:
        p.append(nx.shortest_path_length(maze_graph, weight="weight", source=(temp[0][0], temp[1][0], 0, 1), target=(temp2[0][0], temp2[1][0], d[0], d[1])))
    else:
        p.append(100000000000000000000)
    d = (d[1], -d[0])
mp = min(p)
print(mp)

# P2
paths = []
for i in range(4):
    if p[i] == mp and (temp2[0][0], temp2[1][0], d[0], d[1]) in maze_graph:
        paths.append(nx.all_shortest_paths(maze_graph, weight="weight", source=(temp[0][0], temp[1][0], 0, 1), target=(temp2[0][0], temp2[1][0], d[0], d[1])))
    d = (d[1], -d[0])

locs = set()
for path in paths:
    for p in path:
        for n in p:
            locs.add((n[0], n[1]))
print(len(locs))
