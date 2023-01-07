import random


def monopoly_roll(cur_pos, D, prevD, CC, CH):
    roll1 = random.randint(1, D)
    roll2 = random.randint(1, D)
    if roll1 == roll2:
        if prevD == 2:
            return 10, prevD
        else:
            prevD += 1
    else:
        prevD = 0
    pos = (cur_pos + roll1 + roll2) % 40
    r = random.random()
    if pos == 2 or pos == 17 or pos == 33:  # CC
        crd = CC.pop()
        CC.insert(0, crd)
        if crd == 0:
            return 0, prevD
        elif crd == 1:
            return 10, prevD
        else:
            return pos, prevD
    elif pos == 7 or pos == 22 or pos == 36:  # CH
        crd = CH.pop()
        CH.insert(0, crd)
        if crd == 0:
            return 0, prevD
        elif crd == 1:
            return 10, prevD
        elif crd == 2:
            return 11, prevD
        elif crd == 3:
            return 24, prevD
        elif crd == 4:
            return 39, prevD
        elif crd == 5:
            return 5, prevD
        elif crd == 6 or crd == 7:
            if pos == 7:
                return 15, prevD
            elif pos == 22:
                return 25, prevD
            else:
                return 5, prevD
        elif crd == 8:
            if pos == 7:
                return 12, prevD
            elif pos == 22:
                return 28, prevD
            else:
                return 12, prevD
        elif crd == 9:
            return pos - 3, prevD
        else:
            return pos, prevD
    elif pos == 30:
        return 10, prevD
    else:
        return pos, prevD


occs = [0] * 40
for i in range(1000):
    cp = 0
    pD = 0
    CC = list(range(16))
    CH = list(range(16))
    random.shuffle(CC)
    random.shuffle(CH)
    for j in range(10000):
        cp, pD = monopoly_roll(cp, 4, pD, CC, CH)
        occs[cp] += 1

squares = [x for _, x in sorted(zip(occs, list(range(40))), reverse=True)]
print(squares)
probs = [i / sum(occs) for i in occs]
probs.sort(reverse=True)
print(probs)
