import sympy as sym

def calculate(key, monkeys):
    if monkeys[key].isdigit():
        return int(monkeys[key])
    else:
        comps = monkeys[key].split(' ')
        m1 = comps[0]
        m2 = comps[2]
        if comps[1] == '+':
            return calculate(m1, monkeys) + calculate(m2, monkeys)
        elif comps[1] == '-':
            return calculate(m1, monkeys) - calculate(m2, monkeys)
        elif comps[1] == '*':
            return calculate(m1, monkeys) * calculate(m2, monkeys)
        elif comps[1] == '/':
            return calculate(m1, monkeys) / calculate(m2, monkeys)

def calculate2(key, monkeys):
    if key == 'humn':
        global humn
        return humn
    elif monkeys[key].isdigit():
        return int(monkeys[key])
    else:
        comps = monkeys[key].split(' ')
        m1 = comps[0]
        m2 = comps[2]
        if comps[1] == '+':
            return calculate2(m1, monkeys) + calculate2(m2, monkeys)
        elif comps[1] == '-':
            return calculate2(m1, monkeys) - calculate2(m2, monkeys)
        elif comps[1] == '*':
            return calculate2(m1, monkeys) * calculate2(m2, monkeys)
        elif comps[1] == '/':
            return calculate2(m1, monkeys) / calculate2(m2, monkeys)

# P1
monkeys = {}

with open('input.txt', 'r') as f:
    for line in f:
        comps = line[:-1].split(': ')
        monkeys[comps[0]] = comps[1]

print(calculate('root', monkeys))
        
# P2
humn = sym.Symbol('humn')
comps = monkeys['root'].split(' ')
print(sym.solveset(calculate2(comps[0], monkeys)-calculate2(comps[2], monkeys), humn))