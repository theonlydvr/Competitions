import math

triangles = 0
S = 51

for i in range(1, S ** 2):
    for j in range(1, S ** 2):
        if i != j:
            x1 = i % S
            y1 = math.floor(i / S)
            x2 = j % S
            y2 = math.floor(j / S)
            d1 = x1 ** 2 + y1 ** 2
            d2 = x2 ** 2 + y2 ** 2
            d3 = (x1 - x2) ** 2 + (y1 - y2) ** 2
            if d1 + d2 == d3 or d1 + d3 == d2 or d2 + d3 == d1:
                triangles += 1

print(triangles / 2)
