import lib

# P1
lines = lib.split_file('input.txt')
rules = lines[:lines.index([''])]
updates = lines[lines.index([''])+1:]
updates = [update[0].split(',') for update in updates]
rules = [tuple(rule[0].split('|')) for rule in rules]
rules_dict = {}
for rule in rules:
    rules_dict[(rule[0], rule[1])] = 0
    rules_dict[(rule[1], rule[0])] = 1

total = 0
for update in updates:
    valid = True
    for i, page in enumerate(update):
        for pre in update[:i]:
            if rules_dict[(pre, page)] == 1:
                valid = False
                break
        if not valid:
            break
        for post in update[i+1:]:
            if rules_dict[(page, post)] == 1:
                valid = False
                break
        if not valid:
            break
    if valid:
        total += int(update[len(update) // 2])

print(total)

# P2
total = 0
for update in updates:
    valid = True
    for i, page in enumerate(update):
        for pre in update[:i]:
            if rules_dict[(pre, page)] == 1:
                valid = False
                break
        if not valid:
            break
        for post in update[i+1:]:
            if rules_dict[(page, post)] == 1:
                valid = False
                break
        if not valid:
            break
    if not valid:
        valid = False
        while not valid:
            valid = True
            for i, page in enumerate(update):
                for j, pre in enumerate(update[:i]):
                    if rules_dict[(pre, page)] == 1:
                        valid = False
                        temp = update[i]
                        update[i] = update[j]
                        update[j] = temp
                        break
                if not valid:
                    break
                for j, post in enumerate(update[i + 1:]):
                    if rules_dict[(page, post)] == 1:
                        valid = False
                        temp = update[i]
                        update[i] = update[i+j+1]
                        update[i+j+1] = temp
                        break
                if not valid:
                    break
        total += int(update[len(update) // 2])

print(total)
