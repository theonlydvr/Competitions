# P1
def ordered_list(l1, l2):
    i1 = 0
    i2 = 0
    while i1 < len(l1) and i2 < len(l2):
        if isinstance(l1[i1], int) and isinstance(l2[i2], int):
            if l2[i2] < l1[i1]:
                return -1
            elif l2[i2] > l1[i1]:
                return 1
            else:
                i1 += 1
                i2 += 1
        elif not isinstance([l1[i1]], int) or not isinstance(l2[i2], int):
            if isinstance(l1[i1], int):
                l3 = [l1[i1]]
            else:
                l3 = l1[i1]
            if isinstance(l2[i2], int):
                l4 = [l2[i2]]
            else:
                l4 = l2[i2]
            val = ordered_list(l3, l4)
            if val == 0:
                i1 += 1
                i2 += 1
            else:
                return val
    if i1 == len(l1) and i2 == len(l2):
        return 0
    elif i1 == len(l1):
        return 1
    elif i2 == len(l2):
        return -1

l = 0
l1 = []
l2 = []
count = 0
pn = 0
with open('input.txt', 'r') as f:
    for line in f:
        if l == 0:
            l1 = eval(line[:-1])
            l += 1
        elif l == 1:
            pn += 1
            l2 = eval(line[:-1])
            l += 1
            ordered = ordered_list(l1, l2)
            if ordered >= 0:
                count += pn
        else:
            l = 0

print(count)

# P2
import bisect 

lists = []
with open('input.txt', 'r') as f:
    for line in f:
        if len(line) > 1:
            comp = eval(line[:-1])
            bisect.insort(lists, comp, key=lambda x: ordered_list(comp, x))

bisect.insort(lists, [[2]], key=lambda x: ordered_list([[2]], x))
bisect.insort(lists, [[6]], key=lambda x: ordered_list([[6]], x))

print((lists.index([[2]])+1)*(lists.index([[6]])+1))