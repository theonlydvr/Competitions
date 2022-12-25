# P1
score = 0
with open('input.txt', 'r') as f:
    for line in f:
        opp = line[0]
        me = line[2]
        if opp == 'A':
            if me == 'X':
                score += 4
            elif me == 'Y':
                score += 8
            else:
                score += 3
        elif opp == 'B':
            if me == 'X':
                score += 1
            elif me == 'Y':
                score += 5
            else:
                score += 9
        else:
            if me == 'X':
                score += 7
            elif me == 'Y':
                score += 2
            else:
                score += 6
print(score)

# P2
score = 0
with open('input.txt', 'r') as f:
    for line in f:
        opp = line[0]
        me = line[2]
        if opp == 'A':
            if me == 'X':
                score += 3
            elif me == 'Y':
                score += 4
            else:
                score += 8
        elif opp == 'B':
            if me == 'X':
                score += 1
            elif me == 'Y':
                score += 5
            else:
                score += 9
        else:
            if me == 'X':
                score += 2
            elif me == 'Y':
                score += 6
            else:
                score += 7
print(score)