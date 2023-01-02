import copy

import numpy as np

import lib


def evaluate(grid):
    rows = np.sum(grid, axis=0)
    if np.any(rows == grid.shape[0]):
        return True
    cols = np.sum(grid, axis=1)
    if np.any(cols == grid.shape[1]):
        return True
    return False


def bingo(crds, res, orde):
    for i, o in enumerate(orde):
        for j, card in enumerate(crds):
            for r in range(len(card)):
                for c in range(len(card)):
                    if card[r][c] == o:
                        res[j][r, c] = 1
                        if evaluate(res[j]):
                            total = 0
                            for r2 in range(len(card)):
                                for c2 in range(len(card)):
                                    if res[j][r2][c2] == 0:
                                        total += crds[j][r2][c2]
                            return total * o


def bingo2(crds, res, orde):
    solved = []
    for i, o in enumerate(orde):
        for j, card in enumerate(crds):
            for r in range(len(card)):
                for c in range(len(card)):
                    if card[r][c] == o:
                        res[j][r, c] = 1
                        if j not in solved and evaluate(res[j]):
                            solved.append(j)
                            if len(solved) == len(crds):
                                total = 0
                                for r2 in range(len(card)):
                                    for c2 in range(len(card)):
                                        if res[j][r2][c2] == 0:
                                            total += crds[j][r2][c2]
                                return total * o


data = lib.file_to_ints('input.txt')
order = data[0]

cards = []
results = []

for i in range(1, len(data), 6):
    results.append(np.zeros((5, 5)))
    card = []
    for j in range(i + 1, i + 6):
        card.append(data[j])
    cards.append(card)

# P1
print(bingo(cards, copy.deepcopy(results), order))

# P2
print(bingo2(cards, copy.deepcopy(results), order))
