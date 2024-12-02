import lib

triangles = lib.split_file('p102_triangles.txt', delim='[,]')
contain_origin = 0

for triangle in triangles:
    c = False
    for i in range(3):
        ind1 = 2 * i
        ind2 = 2 * (i + 1) % 6
        if ((triangle[ind1+1] > 0) != (triangle[ind2+1] > 0)) and 0 < (triangle[ind2] - triangle[ind1]) * -triangle[ind1 + 1] / (triangle[ind2+1] - triangle[ind1 + 1]) + triangle[ind1]:
            c = not c
    if c:
        contain_origin += 1

print(contain_origin)
