import networkx as nx

def get_valid_paths(start, stops, tr, total_flow):
    global flow
    global dists
    valid = {}
    valid[''] = tr
    for s in stops:
        if start != '' and s != '':
            dist = dists[(start, s)]
            if tr - (dist + 1) > 0:
                valid[s] = dist + 1
    return valid

def best_future(tr, valid_paths):
    vals = []
    dm = None
    for e in valid_paths.keys():
        if dm is None:
            dm = valid_paths[e]
        if e != '':
            vals.append(rates[e])
        dm = min(dm, valid_paths[e])
    vals.sort(reverse=True)
    future = 0
    i = 0
    while dm is not None and dm < tr and i < len(vals):
        future += vals[i] * (tr - dm)
        i += 1
        dm += 2
    return future

def next_node(tr, valid_paths, total_flow):
    global G
    global flow
    vps = []
    for e in valid_paths.keys():
        trc = tr - valid_paths[e]
        new = list(valid_paths.keys())
        new.remove(e)
        vps.append(get_valid_paths(e, new, trc, total_flow))
    nvalid = 0
    for i, e in enumerate(valid_paths.keys()):
        if e != '':
            trc = tr - valid_paths[e]
            total_flowc = total_flow + rates[e]*trc
            if total_flowc + best_future(trc, vps[i]) > flow:
                nvalid += 1
                next_node(trc, vps[i], total_flowc)
    if nvalid == 0:
        if total_flow > flow:
            flow = total_flow
        
def next_node2(tr, valid_paths, total_flow):
    global G
    global flow
    nvalid = 0
    vp1s = []
    for e1 in valid_paths[0].keys():
        trc1 = tr[0] - valid_paths[0][e1]
        new1 = list(valid_paths[0].keys())
        new1.remove(e1)
        vp1s.append(get_valid_paths(e1, new1, trc1, total_flow))
    vp2s = []
    for e2 in valid_paths[1].keys():
        trc2 = tr[1] - valid_paths[1][e2]
        new2 = list(valid_paths[1].keys())
        new2.remove(e2)
        vp2s.append(get_valid_paths(e2, new2, trc2, total_flow))
    for i, e1 in enumerate(valid_paths[0].keys()):
        for j, e2 in enumerate(valid_paths[1].keys()):
            if e1 != e2:
                trc1 = tr[0] - valid_paths[0][e1]
                trc2 = tr[1] - valid_paths[1][e2]
                total_flowc = total_flow
                if trc1 > 0:
                    total_flowc +=rates[e1] * trc1
                if trc2 > 0:
                    total_flowc +=rates[e2] * trc2
                if trc1 > 0 or trc2 > 0:
                    vp1 = vp1s[i].copy()
                    vp2 = vp2s[j].copy()
                    if e1 in vp2:
                        del vp2[e1]
                    if e2 in vp1:
                        del vp1[e2]
                    if total_flowc + best_future(trc1, vp1) + best_future(trc2, vp2) > flow:
                        nvalid += 1
                        next_node2([trc1, trc2], [vp1, vp2], total_flowc)
    if nvalid == 0:
        if total_flow > flow:
            flow = total_flow

G = nx.Graph()
rates = {}

with open('input.txt', 'r') as f:
    for line in f:
        comps = line.split(' ')
        node = comps[1]
        rate = int(comps[4][5:-1])
        if rate != 0:
            rates[node] = rate
        for i in range(9, len(comps)):
            dest = comps[i][:-1]
            G.add_edge(node, dest)

dists = {}
nodes = list(rates.keys())
nodes.append('AA')

for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        n = nodes[i]
        n2 = nodes[j]
        if n != n2:
            dists[(n, n2)] = nx.shortest_path_length(G, source=n, target=n2)
            dists[(n2, n)] = dists[(n, n2)]

# P1
flow = 0
next_node(30, get_valid_paths('AA',list(rates.keys()),30,0), 0)
print(flow)

# P2
flow = 0
next_node2([26, 26], [get_valid_paths('AA',list(rates.keys()),26,0), get_valid_paths('AA',list(rates.keys()),26,0)], 0)
print(flow)