import math

import numpy as np

def compute_viable(board):
    viable = [[set() for _ in range(9)] for _ in range(9)]
    for r, c in unsolved:
        update_viable(board, viable, r, c)
    return viable


def update_viable(board, viable, r, c):
    if board[r, c] != 0:
        rb = math.floor(r / 3)
        cb = math.floor(c / 3)
        for i in range(9):
            if board[i, c] == 0:
                viable[i][c].add(board[r, c])
                viable[r][i].add(board[r, c])
                viable[rb + math.floor(i / 3)][cb + i % 3].add(board[rb + math.floor(i / 3), cb + i % 3])


boards = []
with open('p096_sudoku.txt') as f:
    board = []
    for line in f:
        if line.startswith('Grid'):
            if len(board) > 0:
                boards.append(np.asarray(board))
            board = []
        else:
            board.append([int(c) for c in line[:-1]])

for board in boards:
    unsolved = []
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                unsolved.append((row, col))
    while len(unsolved) > 0:
        (r, c) = unsolved.pop()
        box = board[math.floor(r/3):math.floor(r/3)+3, math.floor(c/3):math.floor(c/3) + 3].flatten()
        col = board[:, c]
        row = board[r, :]
        bm = cm = rm = []
        for i in range(1, 10):
            if i not in box:
                bm.append(i)
            if i not in col:
                cm.append(i)
            if i not in row:
                rm.append(i)
        if len(bm) == 1:
            board[r, c] = bm[0]
        elif len(cm) == 1:
            board[r, c] = cm[0]
        elif len(rm) == 1:
            board[r, c] = rm[0]
        else:
            unsolved.insert(0, (r, c))
    print(board)
