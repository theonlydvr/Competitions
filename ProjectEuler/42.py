import lib

data = lib.file_to_match('words.txt')[0]
triangles = set()
for i in range(1, 1000):
    triangles.add(int(i*(i+1)/2))

count = 0
for word in data:
    word_sum = 0
    for c in word:
        word_sum += ord(c) - 64
    if word_sum in triangles:
        count += 1

print(count)
