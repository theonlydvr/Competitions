import numpy as np

import lib


def create_plot(plot, food, r, c):
    plot[r, c] = 1
    visited[r, c] = 1
    neighbors = lib.neighbors4(grid, r, c)
    for nr, nc in neighbors:
        if grid[nr, nc] == food and not visited[nr, nc]:
            create_plot(plot, food, nr, nc)


# P1
grid = lib.file_to_mat("input.txt")
visited = np.zeros(grid.shape)
food_dict = {}

for r in range(grid.shape[0]):
    for c in range(grid.shape[1]):
        if not visited[r, c]:
            if grid[r, c] not in food_dict:
                food_dict[grid[r, c]] = []
            new_plot = np.zeros((grid.shape[0] + 2, grid.shape[1] + 2))
            new_plot_temp = np.zeros(grid.shape)
            create_plot(new_plot_temp, grid[r, c], r, c)
            new_plot[1:-1, 1:-1] = new_plot_temp
            food_dict[grid[r, c]].append(new_plot)

total = 0
for plots in food_dict.values():
    for plot in plots:
        area = np.sum(plot)
        perimeter = np.sum(plot[:, 1:] != plot[:, :-1]) + np.sum(plot[1:, :] != plot[:-1, :])
        total += area * perimeter

print(total)

# P2
total = 0
for plots in food_dict.values():
    for plot in plots:
        area = np.sum(plot)
        sides = 0
        transitions = plot[0, 1:] - plot[0, :-1]
        started = False
        for r in range(1, plot.shape[0]):
            trans_new = plot[r, 1:] - plot[r, :-1]
            sides += np.sum((trans_new != transitions) & ((transitions == 0) | (transitions == -trans_new)))
            transitions = trans_new
        transitions = plot[1:, 0] - plot[:-1, 0]
        started = False
        for c in range(1, plot.shape[1]):
            trans_new = plot[1:, c] - plot[:-1, c]
            sides += np.sum((trans_new != transitions) & ((transitions == 0) | (transitions == -trans_new)))
            transitions = trans_new
        # for r in range(1, plot.shape[0] - 1):
        #     for c in range(1, plot.shape[0] - 1):
        #         neighbors = lib.neighbors4(plot, r, c)
        #         count = 0
        #         for nr, nc in neighbors:
        #             count += (plot[r, c] and not plot[nr, nc]) or (not plot[r, c] and plot[nr, nc])
        #         if count == 4:  # single internal
        #             sides += 4
        #         elif count == 3:
        #             sides += 2
        #         elif count == 2 and (plot[r - 1, c] != plot[r + 1, c] or plot[r, c - 1] != plot[r, c + 1]):
        #             sides += 1
        total += area * sides

print(total)
