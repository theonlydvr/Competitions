def palindrome(num):
    for i in range(int(len(num)/2)):
        if num[i] != num[-(i+1)]:
            return False
    return True

count = 0
for i in range(10, 10001):
    lychrel = True
    num = i
    for j in range(50):
        num = num + int(str(num)[::-1])
        if palindrome(str(num)):
            lychrel = False
            break
    if lychrel:
        count += 1

print(count)
