maxsol = 0
maxp = 0

for p in range(5, 1001):
    sols = 0
    for j in range(1, p):
        for k in range(j, p):
            h = (j ** 2 + k ** 2) ** (1/2)
            if h.is_integer():
                if j + k + h == p:
                    sols += 1
                elif j + k + h > p:
                    break
    if sols > maxsol:
        maxsol = sols
        maxp = p

print(maxp)