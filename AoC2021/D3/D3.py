import lib
import numpy as np

# P1
data = lib.file_to_mat('input.txt')
sums = np.sum(data, 0)
gr = ''
er = ''
for i in range(data.shape[1]):
    if sums[i] > data.shape[0]/2:
        gr = gr + '1'
        er = er + '0'
    else:
        gr = gr + '0'
        er = er + '1'
print(int(gr, 2)*int(er, 2))

# P2
gen_valid = list(range(data.shape[0]))
con_valid = list(range(data.shape[0]))
for i in range(data.shape[1]):
    if np.sum(data[gen_valid, i]) >= len(gen_valid)/2:
        most = 1
    else:
        most = 0
    if np.sum(data[con_valid, i]) >= len(con_valid)/2:
        least = 0
    else:
        least = 1
    if len(gen_valid) > 1:
        new_gen = []
        for j in gen_valid:
            if data[j, i] == most:
                new_gen.append(j)
        gen_valid = new_gen
    if len(con_valid) > 1:
        new_con = []
        for j in con_valid:
            if data[j, i] == least:
                new_con.append(j)
        con_valid = new_con
print(int(''.join(str(x) for x in data[gen_valid[0], :]), 2)*int(''.join(str(x) for x in data[con_valid[0], :]), 2))
