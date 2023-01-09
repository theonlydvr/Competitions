import lib
import networkx

data = lib.file_to_ints('p083_matrix.txt')
G = networkx.DiGraph()

for i in range(len(data)):
    for j in range(len(data[0])):
        if i - 1 >= 0:
            G.add_edge((i, j), (i - 1, j), weight=data[i - 1][j])
        if i + 1 < len(data):
            G.add_edge((i, j), (i+1, j), weight=data[i+1][j])
        if j - 1 >= 0:
            G.add_edge((i, j), (i, j - 1), weight=data[i][j - 1])
        if j + 1 < len(data[0]):
            G.add_edge((i, j), (i, j+1), weight=data[i][j+1])

print(networkx.shortest_path_length(G, source=(0, 0), target=(79, 79), weight='weight') + data[0][0])
