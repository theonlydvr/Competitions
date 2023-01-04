import lib

def insert(base, cs, strs, ind, cur):
    if ind == len(base):
        strs.append(cur + cs)
    elif len(cs) == 0:
        strs.append(cur + base[ind:])
    else:
        cur1 = cur + base[ind]
        cur2 = cur + cs[0]
        insert(base, cs, strs, ind+1, cur1)
        insert(base, cs[1:], strs, ind, cur2)


data = lib.split_file('p079_keylog.txt')
sdata = {s[0] for s in data}
data = list(sdata)
data.sort()
guesses = [str(data[0])]
for p in data:
    new_guesses = set()
    p = str(p)
    for g in guesses:
        ind = 0
        li = 0
        for i in range(len(p)):
            while ind < len(g) and p[i] != g[ind]:
                ind += 1
            if ind == len(g):
                break
            li = ind
        if ind == len(g):
            adds = []
            insert(g[li+1:], p[i:], adds, 0, '')
            for a in adds:
                c = a[0]
                for j in range(1, len(a)):
                    if c[-1] != a[j]:
                        c += a[j]
                new_guesses.add(g[:li+1]+c)
        else:
            new_guesses.add(g)
    smallest = min([len(g) for g in new_guesses])
    guesses = {g for g in new_guesses if len(g) == smallest}

print(guesses.pop()[1:])
