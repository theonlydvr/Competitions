import math
from decimal import *

getcontext().prec = 1000

sum_odd = 0
for i in range(2, 10001):
    if not math.sqrt(i).is_integer():
        cur = Decimal(i).sqrt()
        j = 1
        div = start = math.floor(cur)
        while div != start * 2:
            cur = Decimal(1) / (cur - div)
            div = math.floor(cur)
            j += 1
        if (j - 1) % 2 == 1:
            sum_odd += 1

print(sum_odd)
