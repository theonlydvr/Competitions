import math

import numpy as np


def is_viable(board, sq):
    rb = math.floor(sq / 9 / 3)
    cb = math.floor(sq % 9 % 3)
    l = board[math.floor(sq / 9), :]
    l = l[l != 0]
    if len(np.unique(l)) != len(l):
        return False
    l = board[:, sq % 9]
    l = l[l != 0]
    if len(np.unique(l)) != len(l):
        return False
    l = board[3 * rb:3 * rb + 3, 3 * cb:3 * cb + 3]
    l = l[l != 0]
    if len(np.unique(l)) != len(l):
        return False
    return True


def solve(orig, brd, sq):
    if sq == 81:
        return brd
    else:
        while sq < 81 and orig[math.floor(sq / 9), sq % 9] != 0:
            sq += 1
        if sq == 81:
            return brd
        found = False
        for i in range(1, 10):
            brd[math.floor(sq / 9), sq % 9] = i
            if is_viable(brd, sq):
                found = True
                check = solve(orig, brd, sq+1)
                if check is not None:
                    return check
            brd[math.floor(sq / 9), sq % 9] = 0
        if not found:
            return None


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
boards.append(np.asarray(board))

all_sum = 0
i = 0

for board in boards:
    i += 1
    board2 = board.copy()
    board2 = solve(board, board2, 0)
    if board2 is None:
        print()
    else:
        all_sum += int(''.join([str(i) for i in list(board2[0, 0:3])]))

print(all_sum)
