from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


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


"""
#ip 5
0 seti 123 0 4          # r[4] = 123
1 bani 4 456 4          # r[4] = r[4] & 456
2 eqri 4 72 4           # r[4] = r[4] == 72 = 1
3 addr 4 5 5            # r[5] = r[4] + r[5] ==> jumpto 5
4 seti 0 0 5            # r[5] = 0 ==> jumpto 0 if bani is bugged
5 seti 0 8 4            # r[4] = 0
6 bori 4 65536 3        # r[3] = r[4] | 65536
7 seti 707129 0 4       # r[4] = 707129
8 bani 3 255 2          # r[2] = r[3] & 255
9 addr 4 2 4            # r[4] = r[4] + r[2]
10 bani 4 16777215 4    # r[4] = r[4] & 16777215
11 muli 4 65899 4       # r[4] = r[4] * 65899
12 bani 4 16777215 4    # r[4] = r[4] & 16777215
13 gtir 256 3 2         # r[2] = 256 > r[3] 
14 addr 2 5 5           # r[5] = r[2] + r[5] ==> jumpto 16
15 addi 5 1 5           # r[5] = r[5] + 1 ==> jumpto 17
16 seti 27 6 5          # r[5] = 27 ==> jumpto 28
17 seti 0 7 2           # r[2] = 0
18 addi 2 1 1           # r[1] = r[2] + 1
19 muli 1 256 1         # r[1] = r[1] * 256 
20 gtrr 1 3 1           # r[1] = r[1] > r[3] 
21 addr 1 5 5           # r[5] = r[1] + r[5] ==> jumpto 23
22 addi 5 1 5           # r[5] = r[5] + 1 ==> jumpto 24 
23 seti 25 2 5          # r[5] = 25 ==> jumpto 26
24 addi 2 1 2           # r[2] = r[2] + 1
25 seti 17 1 5          # r[5] = 17 ==> jumpto 18
26 setr 2 4 3           # r[3] = r[2]
27 seti 7 4 5           # r[5] = 7 ==> jumpto 8
28 eqrr 4 0 2           # r[2] = r[4] == r[0]
29 addr 2 5 5           # r[5] = r[2] + r[5] ==> exit programm
30 seti 5 2 5           # r[5] = 5 ==> jumpto 6


relevant:

5 seti 0 8 4            # r[4] = 0                  init
6 bori 4 65536 3        # r[3] = r[4] | 65536       loop entry, calc r[3] and r[4]
7 seti 707129 0 4       # r[4] = 707129
8 bani 3 255 2          # r[2] = r[3] & 255         loop entry, calc r[3] and r[4]
9 addr 4 2 4            # r[4] = r[4] + r[2]
10 bani 4 16777215 4    # r[4] = r[4] & 16777215
11 muli 4 65899 4       # r[4] = r[4] * 65899
12 bani 4 16777215 4    # r[4] = r[4] & 16777215
13 gtir 256 3 2         # r[2] = 256 > r[3] 
14 addr 2 5 5           # r[5] = r[2] + r[5]        ==> jumpto 16
15 addi 5 1 5           # r[5] = r[5] + 1           ==> jumpto 17
16 seti 27 6 5          # r[5] = 27                 ==> jumpto 28
17 seti 0 7 2           # r[2] = 0                  starts: divide r[3] by 256 
18 addi 2 1 1           # r[1] = r[2] + 1
19 muli 1 256 1         # r[1] = r[1] * 256 
20 gtrr 1 3 1           # r[1] = r[1] > r[3] 
21 addr 1 5 5           # r[5] = r[1] + r[5]        ==> jumpto 23
22 addi 5 1 5           # r[5] = r[5] + 1           ==> jumpto 24 
23 seti 25 2 5          # r[5] = 25                 ==> jumpto 26
24 addi 2 1 2           # r[2] = r[2] + 1
25 seti 17 1 5          # r[5] = 17                 ==> jumpto 18
26 setr 2 4 3           # r[3] = r[2]               ends: divide r[3] by 256
27 seti 7 4 5           # r[5] = 7                  ==> jumpto 8
28 eqrr 4 0 2           # r[2] = r[4] == r[0]       relevant comparison r[4] and r[0]
29 addr 2 5 5           # r[5] = r[2] + r[5]        ==> exit programm
30 seti 5 2 5           # r[5] = 5                  ==> jumpto 6

same as ==> 

r[4] = 0
r[3] = r[4] | 65536 #line 6
r[4] = 707129
r[4] = (((r[4] + (r[3] & 255)) & 16777215) * 65899) & 16777215 #line 8
if 256 > r[3]:
    if r[0] == r[4]:
        exit()
    else:
        goto line 6
else:
    r[3] = r[3] // 256
    goto line 8

"""

# reimplementation of the intended workflow.
def f_own():
    vals = []
    r = defaultdict(int)
    while True:
        r[3] = r[4] | 65536
        r[4] = 707129
        for _ in range(3):
            r[4] = (((r[4] + (r[3] & 255)) & 16777215) * 65899) & 16777215
            r[3] = r[3] // 256
        if r[4] in vals:
            return vals
        vals.append(r[4])

# run original code. each time the input gets matched (line 28), log the expected value. end when loop detected.
def f_slow(p1):
    vals = []
    while registers[ip_reg] < len(instructions):
        if registers[ip_reg] == 28:
            if registers[4] in vals:
                return vals
            vals.append(registers[4])
            if p1:
                return vals

        l = instructions[registers[ip_reg]]
        op, a, b, c = l.split(" ")
        globals()[op](int(a), int(b), int(c))
        registers[ip_reg] += 1


# same as f_slow, but the expensive division loop gets replaced (lines 17-27)
def f_improved():
    vals = []
    while registers[ip_reg] < len(instructions):
        if registers[ip_reg] == 28:
            if registers[4] in vals:
                return vals
            vals.append(registers[4])

        if registers[ip_reg] == 17:  # replace inefficient division
            registers[3] = registers[3] // 256
            registers[ip_reg] = 27

        l = instructions[registers[ip_reg]]
        op, a, b, c = l.split(" ")
        globals()[op](int(a), int(b), int(c))
        registers[ip_reg] += 1




print("Rewritten implementation:")
res_own = f_own()
p1 = res_own[0]
p2 = res_own[-1]
print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
print()

print("Improved original implementation:")
ip_reg = int(lines[0][-1])
instructions = lines[1:]
registers = defaultdict(int)
res_improved = f_improved()
p1 = res_improved[0]
p2 = res_improved[-1]
print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
print()

print("Original implementation (slow!):")

registers = defaultdict(int)
p1 = f_slow(True)[0]

print("Part 1: " + str(p1))

registers = defaultdict(int)
p2 = f_slow(False)[-1]

print("Part 2: " + str(p2))
