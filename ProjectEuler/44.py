import math
from queue import PriorityQueue


def is_pentagonal(n):
    n = (1 + math.sqrt(24 * n + 1)) / 6
    return (n - int(n)) == 0


valid = False
m = 2
while not valid:
    n = m - 1
    while n > 0:
        if is_pentagonal(m*(3*m-1)/2 - n*(3*n-1)/2) and is_pentagonal(m*(3*m-1)/2 + n*(3*n-1)/2):
            print(m*(3*m-1)/2 - n*(3*n-1)/2)
            valid = True
            break
        n -= 1
    if valid:
        break
    m += 1
