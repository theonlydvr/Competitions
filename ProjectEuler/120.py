tot = 0
for a in range(3, 1001):
    mx = 0
    mxn = 0
    stopping = 100
    n = 1
    while n < stopping:
        if ((a-1) ** n + (a+1) ** n) % a ** 2 > mx:
            mx = ((a - 1) ** n + (a + 1) ** n) % a ** 2
            mxn = n
            if stopping - n < 800:
                stopping += 800
        n += 1
    tot += mx
print(tot)
