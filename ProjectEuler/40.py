num = 1
counter = 1
i = 1
done = False
ind = 1
while not done:
    si = str(num)
    for c in si:
        if i == ind:
            counter *= int(c)
            ind *= 10
            if ind > 1000000:
                done = True
                break
        i += 1
    num += 1

print(counter)
