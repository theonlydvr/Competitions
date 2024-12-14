from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np

import lib


@dataclass
class Robot:
    p: tuple
    v: tuple


# P1
lines = lib.split_file('input.txt')
robots = []
for line in lines:
    p = line[0].split('=')[1].split(',')
    v = line[1].split('=')[1].split(',')
    robots.append(Robot((int(p[1]), int(p[0])), (int(v[1]), int(v[0]))))

gr = 103
gc = 101
fig = plt.figure()

for i in range(10000):
    for robot in robots:
        robot.p = ((robot.p[0] + robot.v[0]) % gr, (robot.p[1] + robot.v[1]) % gc)

    grid = np.zeros((gr, gc))
    for robot in robots:
        grid[robot.p[0], robot.p[1]] += 1
    temp = np.sum(grid != np.flip(grid, 0))
    if np.sum(grid[:, 23] + np.sum(grid[:, 53])) > 3000:
        plt.clf()
        plt.imshow(grid[:, 23:54])
        plt.title(i + 1)
        # plt.ion()
        plt.show()
        # plt.pause(0.5)

print(np.sum(grid[:gr // 2, :gc // 2]) * np.sum(grid[(gr + 1) // 2:, :gc // 2]) * np.sum(grid[(gr + 1) // 2:, (gc + 1) // 2:]) * np.sum(grid[:gr // 2, (gc + 1) // 2:]))
