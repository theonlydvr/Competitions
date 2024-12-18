import lib

# P1
lines = lib.split_file('test3.txt')
A = int(lines[0][-1])
B = int(lines[1][-1])
C = int(lines[2][-1])
program = [int(i) for i in lines[-1][-1].split(',')]

ip = 0
output = []

while ip < len(program) - 1:
    opcode = program[ip]
    lit_operand = program[ip + 1]
    operand = program[ip + 1]

    if operand == 4:
        operand = A
    elif operand == 5:
        operand = B
    elif operand == 6:
        operand = C

    if opcode == 0:
        A = A // (2 ** operand)
    elif opcode == 1:
        B = B ^ lit_operand
    elif opcode == 2:
        B = operand % 8
    elif opcode == 3:
        if A != 0:
            ip = lit_operand - 2
    elif opcode == 4:
        B = B ^ C
    elif opcode == 5:
        output.append(operand % 8)
    elif opcode == 6:
        B = A // (2 ** operand)
    elif opcode == 7:
        C = A // (2 ** operand)
    ip += 2

print(output, sep=",")

# P2
Ao = int(lines[0][-1])
Bo = int(lines[1][-1])
Co = int(lines[2][-1])
program = [int(i) for i in lines[-1][-1].split(',')]

A = "A"
B = "0"
C = "0"
ip = 0
output = []

while len(output) < len(program):
    opcode = program[ip]
    lit_operand = program[ip + 1]
    operand = program[ip + 1]

    if operand == 4:
        operand = A
    elif operand == 5:
        operand = B
    elif operand == 6:
        operand = C

    if opcode == 0:
        A = f"({A}) // (2 ** ({operand}))"
    elif opcode == 1:
        B = f"({B}) ^ {lit_operand}"
    elif opcode == 2:
        B = f"(({operand}) % 8)"
    elif opcode == 3:
        if A != "0":
            ip = lit_operand - 2
    elif opcode == 4:
        B = f"(({B}) ^ ({C}))"
    elif opcode == 5:
        output.append(f"(({operand}) % 8)")
    elif opcode == 6:
        B = f"({A}) // (2 ** ({operand}))"
    elif opcode == 7:
        C = f"({A}) // (2 ** ({operand}))"
    ip += 2

rules = {}
for N in range(2 ** 10):
    out2 = (N % 8) ^ 1 ^ 4 ^ (N // (2 ** ((N % 8) ^ 1))) % 8
    if out2 not in rules:
        rules[out2] = [N]
    else:
        rules[out2].append(N)

sequences = [["X"] * len(program) * 10 * 3]

for i, c in enumerate(program):
    new_sequences = []
    for seq in sequences:
        shifted = seq[:len(seq) if i == 0 else -3*i]
        for N in rules[c]:
            bstr = list(f'{N:010b}')
            if all(c1 == c2 or c1 == "X" for c1, c2 in zip(shifted[-10:], bstr)):
                prop = shifted[:-10] + bstr + seq[len(seq) if i == 0 else -3*i:]
                new_sequences.append(list(p1 if p2 == "X" else p2 for p1, p2 in zip(seq, prop)))
    sequences = new_sequences

mseq = -1
for seq in sequences:
    val = int(''.join(seq).replace("X", "0"), 2)
    mseq = val if mseq == -1 or val < mseq else mseq

print(mseq)
