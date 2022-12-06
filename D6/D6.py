# P1
counter = 0
buffer = []
with open('input.txt', 'r') as f:
    c = f.read(1)
    while c:
        buffer.insert(0, c)
        counter += 1
        if counter > 4:
            buffer.pop()
        if len(set(buffer))==4:
            break
        c = f.read(1)

print(counter)

# P2
counter = 0
buffer = []
with open('input.txt', 'r') as f:
    c = f.read(1)
    while c:
        buffer.insert(0, c)
        counter += 1
        if counter > 14:
            buffer.pop()
        if len(set(buffer))==14:
            break
        c = f.read(1)

print(counter)