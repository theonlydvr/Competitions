import lib
import numpy as np


def pokerify(row):
    c = []
    s = []
    for card in row:
        val = card[:-1]
        if val == 'A':
            c.append(14)
        elif val == 'K':
            c.append(13)
        elif val == 'Q':
            c.append(12)
        elif val == 'J':
            c.append(11)
        elif val == 'T':
            c.append(10)
        else:
            c.append(int(val))
        s.append(card[-1])
    rown = [x for y, x in sorted(zip(c, row), reverse=True)]
    c.sort(reverse=True)
    if len(set(s)) == 1 and len(c) == 5:
        if c == list(range(14, 9, -1)):  # Royal flush
            return 'S'
        elif np.all(np.diff(c) == -1):  # Straight flush
            return 'R{:0>2}'.format(np.max(c))
    counts = {}
    for card in c:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1
    if np.max(list(counts.values())) == 4:  # Four of a kind
        val = list(counts.keys())[list(counts.values()).index(4)]
        return 'Q{:0>2}_'.format(val) + pokerify([rown[i] for i in list(range(len(c))) if c[i] != val])
    if set(counts.values()) == {3, 2}:  # Full house
        return 'P{:0>2}_{:0>3}'.format(list(counts.keys())[list(counts.values()).index(3)], list(counts.keys())[list(counts.values()).index(2)])
    if len(c) == 5:
        if len(set(s)) == 1:  # Flush
            return 'O' + '_0'.join(['{:0>2}'.format(card) for card in c])
        elif np.all(np.diff(c) == -1):  # Straight
            return 'N{:0>2}'.format(np.max(c))
    if np.max(list(counts.values())) == 3:  # Three of a kind
        val = list(counts.keys())[list(counts.values()).index(3)]
        return 'M{:0>2}_'.format(val) + pokerify([rown[i] for i in range(len(c)) if c[i] != val])
    elif np.max(list(counts.values())) == 2:
        count2 = list(counts.values()).count(2)
        if count2 == 2:  # Two pairs
            keys = list(counts.keys())
            vals = [i for i, x in enumerate(list(counts.values())) if x == 2]
            return 'L{:0>2}_{:0>3}_K{:0>2}'.format(keys[vals[0]], keys[vals[1]], keys[list(counts.values()).index(1)])
        else:  # One pair
            val = list(counts.keys())[list(counts.values()).index(2)]
            return 'K{:0>2}_'.format(val) + pokerify([rown[i] for i in list(range(len(c))) if c[i] != val])
    else:  # High
        return 'J' + '_0'.join(['{:0>2}'.format(card) for card in c])


data = lib.split_file('54_poker.txt')

count = 0
for row in data:
    count += pokerify(row[:5]) > pokerify(row[5:])

print(count)
