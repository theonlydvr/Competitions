i = 286
T = i*(i+1)/2
while not ((1 + (1 + 12 * 2 * T) ** (1/2)) / 6).is_integer() or not ((1 + (1 + 8 * T) ** (1/2)) / 4).is_integer():
    i += 1
    T = i * (i+1) / 2
print(T)
