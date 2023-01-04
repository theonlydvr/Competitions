cubes = {}
for i in range(10000):
    lst = list(str(i ** 3))
    lst.sort()
    key = ''.join(lst)
    if key in cubes:
        cubes[key].append(i)
    else:
        cubes[key] = [i]

for i in range(10000):
    lst = list(str(i ** 3))
    lst.sort()
    key = ''.join(lst)
    if len(cubes[key]) == 5:
        print(i ** 3)
        break
