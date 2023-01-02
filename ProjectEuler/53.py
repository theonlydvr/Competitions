import math

count = 0
for i in range(1, 101):
    for j in range(0, i+1):
        if math.factorial(i)/(math.factorial(j)*math.factorial(i-j)) > 1000000:
            count += 1

print(count)