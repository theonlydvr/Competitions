i = 1
count = 0
while len(str(9 ** i)) == i:
    for j in range(1, 10):
        if len(str(j ** i)) == i:
            count += 1
    i += 1
print(count)
