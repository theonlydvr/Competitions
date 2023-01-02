from fractions import Fraction
f = Fraction(1, 1)
for i in range(10, 100):
    for j in range(i + 1, 100):
        si = str(i)
        sj = str(j)
        fn = Fraction(i, j)
        for c in si:
            if c != '0' and c in sj:
                i1 = int(si.replace(c, '', 1))
                i2 = int(sj.replace(c, '', 1))
                if i2 != 0:
                    fn2 = Fraction(i1, i2)
                    if fn == fn2:
                        f = f * fn2

print(f)
