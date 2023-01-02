import lib

data = lib.file_to_match('words.txt')[0]
anagrams = {}
for word in data:
    sword = ''.join(sorted(word))
    if sword in anagrams:
        anagrams[sword].append(word)
    else:
        anagrams[sword] = [word]
anagrams = {key: anagrams[key] for key in anagrams.keys() if len(anagrams[key]) > 1}
squares = []
i = 1
while i ** 2 < 1000000000:
    squares.append(i ** 2)
    i += 1
sqanagrams = {}
for num in squares:
    snum = ''.join(sorted(str(num)))
    if snum in sqanagrams:
        sqanagrams[snum].append(str(num))
    else:
        sqanagrams[snum] = [str(num)]
sqanagrams = {key: sqanagrams[key] for key in sqanagrams.keys() if len(sqanagrams[key]) > 1}

keys = [k for _, k in sorted(zip([max(sqanagrams[k]) for k in sqanagrams.keys()], list(sqanagrams.keys())), reverse=True)]

mx = 0

for key in keys:
    sdict = {k: anagrams[k] for k in anagrams.keys() if len(k) == len(key)}
    for num in sqanagrams[key]:
        for k in sdict.keys():
            for i in range(len(sdict[k])):
                tdict = {}
                valid = True
                for l in range(len(k)):
                    if sdict[k][i][l] in tdict:
                        if tdict[sdict[k][i][l]] != num[l]:
                            valid = False
                            break
                    else:
                        tdict[sdict[k][i][l]] = num[l]
                if not valid or len(set(tdict.values())) != len(tdict):
                    break
                comp1 = ''.join([tdict[c] for c in sdict[k][i]])
                for j in range(i + 1, len(sdict[k])):
                    comp2 = ''.join([tdict[c] for c in sdict[k][j]])
                    if comp2 in sqanagrams[key]:
                        mx = max(mx, int(comp1), int(comp2))
print(mx)
