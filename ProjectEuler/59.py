import lib
from statistics import mode

data = lib.split_file('p059_cipher.txt', delim=',')[0]
for a in range(97, 123):
    for b in range(97, 123):
        for c in range(97, 123):
            key = [a, b, c] * int(len(data) / 3)
            decrypted = [data[i] ^ key[i] for i in range(len(data))]
            dstr = ''.join([chr(d) for d in decrypted])
            if mode(dstr) == ' ':
                print(dstr)
                print(sum(decrypted))

