import numpy as np
from scipy.spatial.distance import cdist

import lib

track = lib.file_to_mat('input.txt')

start = np.where(track == 'S')
end = np.where(track == 'E')
end = (int(end[0][0]), int(end[1][0]))

path = [(int(start[0]), int(start[1]))]
dpath = {path[-1]: 0}
p = 1
while path[-1] != end:
    neighbors = lib.neighbors4(track, path[-1][0], path[-1][1])
    for n in neighbors:
        if track[n[0], n[1]] != '#' and n not in dpath:
            path.append(n)
            dpath[n] = p
            p += 1

saving_target = 100
total = 0
for i, l in enumerate(path):
    neighbors = lib.neighbors4(track, l[0], l[1])
    for n in neighbors:
        if track[n[0], n[1]] == '#':
            d = (n[0] - l[0], n[1] - l[1])
            if 0 <= n[0] + d[0] < track.shape[0] and 0 <= n[1] + d[1] < track.shape[1] and track[n[0] + d[0], n[1] + d[1]] != '#':
                total += dpath[n[0] + d[0], n[1] + d[1]] - (i + 2) >= saving_target

print(total)

# P2
coords = np.where(track != '')
all_coords = np.stack((coords[0], coords[1]), axis=1)
valid = track != '#'

total = 0
for i, l in enumerate(path):
    dists = cdist(all_coords, np.asarray(l)[np.newaxis, ...], 'cityblock').reshape(track.shape)
    cheats = np.where(valid & (dists <= 20))
    for c in range(cheats[0].shape[0]):
        total += dpath[cheats[0][c], cheats[1][c]] - (i + dists[cheats[0][c], cheats[1][c]]) >= saving_target

print(total)
