import numpy as np

import lib

# P1
lines = lib.split_file('input.txt')
file_system = np.nan * np.zeros(sum(int(i) for i in lines[0][0]))
ind = 0
ID = 0
for i, c in enumerate(lines[0][0]):
    if i % 2 == 0:
        fill = ID
    else:
        fill = np.nan
    file_system[ind:ind+int(c)] = fill
    ind += int(c)
    ID += i % 2 == 0

free_index = 0
grab_index = file_system.shape[0] - 1

while free_index < grab_index:
    while not np.isnan(file_system[free_index]):
        free_index += 1
    while np.isnan(file_system[grab_index]):
        grab_index -= 1
    if free_index < grab_index:
        file_system[free_index] = file_system[grab_index]
        file_system[grab_index] = np.nan

print(sum(file_system[i] * i for i in range(file_system.shape[0] - np.sum(np.isnan(file_system)))))

# P2
file_system = np.nan * np.zeros(sum(int(i) for i in lines[0][0]))
ind = 0
ID = 0
blobs = []
files = []

for i, c in enumerate(lines[0][0]):
    if i % 2 == 0:
        fill = ID
        files.append((ind, int(c)))
    else:
        blobs.append((ind, int(c)))
        fill = np.nan
    file_system[ind:ind+int(c)] = fill
    ind += int(c)
    ID += i % 2 == 0

file_ind = len(files) - 1
while file_ind >= 0:
    for sp_ind, sp in enumerate(blobs):
        if sp_ind < file_ind and files[file_ind][1] <= sp[1]:
            file_system[sp[0]:sp[0] + files[file_ind][1]] = file_ind
            blobs[sp_ind] = (sp[0] + files[file_ind][1], sp[1] - files[file_ind][1])
            file_system[files[file_ind][0]:files[file_ind][0]+files[file_ind][1]] = np.nan
            break

    file_ind -= 1

print(np.nansum(file_system * np.arange(file_system.shape[0])))
