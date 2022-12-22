class Node:
    def __init__(self, wall, row, col):
        self.l = None
        self.r = None
        self.u = None
        self.d = None
        self.wall = wall
        self.row = row
        self.col = col

# P1
facings = ['r', 'd', 'l', 'u']
i_next = False
root = None
row0 = []
row = []
r = 0
with open('input.txt', 'r') as f:
    for line in f:
        if line[:-1] == '':
            i_next = True
        elif i_next:
            for i, n in enumerate(row0):
                n.u = row[i]
                row[i].d = n
            num = ""
            facing = 0
            cur_node = root
            for c in line[:-1]:
                if c.isdigit():
                    num += c
                else:
                    i = 0
                    while i < int(num):
                        # print("{} {} {}".format(cur_node.row, cur_node.col, facings[facing]))
                        if not getattr(cur_node, facings[facing]).wall:
                            cur_node = getattr(cur_node, facings[facing])
                        else:
                            break
                        i += 1
                    if c == 'R':
                        facing = (facing+1)%4
                    else:
                        facing = (facing-1)%4
                    num = ""
            i = 0
            while i < int(num):
                # print("{} {} {}".format(cur_node.row, cur_node.col, facings[facing]))
                if not getattr(cur_node, facings[facing]).wall:
                    cur_node = getattr(cur_node, facings[facing])
                else:
                    break
                i += 1
            print(1000*cur_node.row + 4*cur_node.col + facing)
        else:
            r += 1
            l_most = None
            for i, c in enumerate(line[:-1]):
                if i >= len(row0):
                    row0.append(None)
                if c != ' ':
                    node = Node(c=='#',r,i+1)
                    if l_most is None:
                        l_most = node
                    if root is None:
                        root = node
                    if i-1 >= 0:
                        node.l = row[i-1]
                    if row[i-1] is not None:
                        row[i-1].r = node
                    if i < len(row):
                        node.u = row[i]
                        if row[i] is not None:
                            row[i].d = node
                        row[i] = node
                    else:
                        row.append(node)
                    if row0[i] is None:
                        row0[i] = node
                elif i >= len(row):
                    row.append(None)
            l_most.l = node
            node.r = l_most
            
# P2
facings = ['r', 'd', 'l', 'u']
i_next = False
root = None
row0 = []
rowl = []
rowr = []
row = []
r = 0
with open('input.txt', 'r') as f:
    for line in f:
        if line[:-1] == '':
            i_next = True
        elif i_next:
            sl = int(len(row)/3)
            for i in range(sl,sl*2):
                rowl[i].l=(1, row0[i-sl])
                row0[i-sl].u=(0, rowl[i])
                
                row[i].d=(2, rowr[i+sl*2])
                rowr[i+sl*2].r=(3, row[i])
                
                rowr[i+sl].r = (2, rowr[2*sl-i-1])
                rowr[2*sl-i-1].r = (2, rowr[i+sl])
                
                rowl[i-sl].l = (0, rowl[4*sl-i-1])
                rowl[4*sl-i-1].l = (0, rowl[i-sl])
                
                row0[i+sl].u = (3, row[i-sl])
                row[i-sl].d = (1, row0[i+sl])
                
                row0[i].u = (0, rowl[i+sl*2])
                rowl[i+sl*2].l = (1, row0[i])
                
                rowr[i].r = (3, row[i+sl])
                row[i+sl].d = (2, rowr[i])
            
            num = ""
            facing = 0
            cur_node = root
            for c in line[:-1]:
                if c.isdigit():
                    num += c
                else:
                    i = 0
                    while i < int(num):
                        print("{} {} {}".format(cur_node.row, cur_node.col, facings[facing]))
                        if not getattr(cur_node, facings[facing])[1].wall:
                            facing, cur_node = getattr(cur_node, facings[facing])
                        else:
                            break
                        i += 1
                    if c == 'R':
                        facing = (facing+1)%4
                    else:
                        facing = (facing-1)%4
                    num = ""
            i = 0
            while i < int(num):
                # print("{} {} {}".format(cur_node.row, cur_node.col, facings[facing]))
                if not getattr(cur_node, facings[facing])[1].wall:
                    facing, cur_node = getattr(cur_node, facings[facing])
                else:
                    break
                i += 1
            print(1000*cur_node.row + 4*cur_node.col + facing)
        else:
            r += 1
            l_most = None
            for i, c in enumerate(line[:-1]):
                if i >= len(row0):
                    row0.append(None)
                if c != ' ':
                    node = Node(c=='#',r,i+1)
                    if l_most is None:
                        l_most = node
                    if root is None:
                        root = node
                    if i-1 >= 0:
                        node.l = (2, row[i-1])
                    if row[i-1] is not None:
                        row[i-1].r = (0, node)
                    if i < len(row):
                        node.u = (3, row[i])
                        if row[i] is not None:
                            row[i].d = (1, node)
                        row[i] = node
                    else:
                        row.append(node)
                    if row0[i] is None:
                        row0[i] = node
                elif i >= len(row):
                    row.append(None)
            rowl.append(l_most)
            rowr.append(node)