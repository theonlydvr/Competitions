import math

import lib

data = lib.file_to_ints('p099_base_exp.txt')
ind = 0
highest = data[0][1]*math.log(data[0][0])

for i in range(1, len(data)):
    val = data[i][1]*math.log(data[i][0])
    if val > highest:
        highest = val
        ind = i

print(ind + 1)

