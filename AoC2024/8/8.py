import math

import lib
import numpy as np

# P1
grid = lib.file_to_mat("input.txt")
frequencies = np.unique(grid)[1:]
antinodes = np.zeros(grid.shape)

for freq in frequencies:
    locs = np.where(grid == freq)
    for i in range(len(locs[0])):
        for j in range(i + 1, len(locs[0])):
            vec = (locs[0][i] - locs[0][j], locs[1][i] - locs[1][j])
            an0 = (locs[0][i] + vec[0], locs[1][i] + vec[1])
            if 0 <= an0[0] < grid.shape[0] and 0 <= an0[1] < grid.shape[1]:
                antinodes[an0[0], an0[1]] = 1
            an1 = (locs[0][j] - vec[0], locs[1][j] - vec[1])
            if 0 <= an1[0] < grid.shape[0] and 0 <= an1[1] < grid.shape[1]:
                antinodes[an1[0], an1[1]] = 1

print(np.sum(antinodes))

# P2
antinodes = np.zeros(grid.shape)

for freq in frequencies:
    locs = np.where(grid == freq)
    for i in range(len(locs[0])):
        for j in range(i + 1, len(locs[0])):
            vec = (locs[0][i] - locs[0][j], locs[1][i] - locs[1][j])
            g = math.gcd(vec[0], vec[1])
            vec = (vec[0] // g, vec[1] // g)
            an0 = (locs[0][i], locs[1][i])
            while 0 <= an0[0] < grid.shape[0] and 0 <= an0[1] < grid.shape[1]:
                antinodes[an0[0], an0[1]] = 1
                an0 = (an0[0] + vec[0], an0[1] + vec[1])
            an0 = (locs[0][i], locs[1][i])
            while 0 <= an0[0] < grid.shape[0] and 0 <= an0[1] < grid.shape[1]:
                antinodes[an0[0], an0[1]] = 1
                an0 = (an0[0] - vec[0], an0[1] - vec[1])

print(np.sum(antinodes))
