import re


def all_ints_in_string(s):
    return [int(n) for n in re.findall(r'-?\d+', s)]


def addr(a, b, c):
    registers[c] = registers[a] + registers[b]


def addi(a, b, c):
    registers[c] = registers[a] + b


def mulr(a, b, c):
    registers[c] = registers[a] * registers[b]


def muli(a, b, c):
    registers[c] = registers[a] * b


def banr(a, b, c):
    registers[c] = registers[a] & registers[b]


def bani(a, b, c):
    registers[c] = registers[a] & b


def borr(a, b, c):
    registers[c] = registers[a] | registers[b]


def bori(a, b, c):
    registers[c] = registers[a] | b


def setr(a, b, c):
    registers[c] = registers[a]


def seti(a, b, c):
    registers[c] = a


def gtir(a, b, c):
    registers[c] = int(a > registers[b])


def gtri(a, b, c):
    registers[c] = int(registers[a] > b)


def gtrr(a, b, c):
    registers[c] = int(registers[a] > registers[b])


def eqir(a, b, c):
    registers[c] = int(a == registers[b])


def eqri(a, b, c):
    registers[c] = int(registers[a] == b)


def eqrr(a, b, c):
    registers[c] = int(registers[a] == registers[b])


def set_registers(vals):
    for i in range(4):
        registers[i] = vals[i]


def validate_registers(vals):
    valid = True
    for i in range(4):
        valid &= registers[i] == vals[i]
    return valid


file = open("input.txt").read()
samples, lower = file.split("\n\n\n\n")

operations = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

registers = {}
candidates = {}

for op in operations:
    candidates[op] = set(range(16))

p1 = 0
for sample in samples.split("\n\n"):
    sample = sample.split("\n")

    before = all_ints_in_string(sample[0])
    command = all_ints_in_string(sample[1])
    after = all_ints_in_string(sample[2])
    opcode, a, b, c = command

    count = 0

    for op in operations:
        set_registers(before)
        op(a, b, c)
        count += validate_registers(after)
        if not validate_registers(after):
            candidates[op].discard(opcode)

    if count >= 3:
        p1 += 1

lookup = {}
while len(lookup) != len(candidates):
    for c in candidates:
        if len(candidates[c]) == 1 and c not in lookup.values():
            opcode = candidates[c].pop()
            lookup[opcode] = c
            for d in candidates:
                candidates[d].discard(opcode)

set_registers([0, 0, 0, 0])
for line in lower.split("\n"):
    opcode, a, b, c = all_ints_in_string(line)
    lookup[opcode](a, b, c)

p2 = registers[0]

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
