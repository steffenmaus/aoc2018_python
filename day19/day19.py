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




'''
after init:
r[0] = 0
r[1] = 10551292
r[2] = 1
r[3] = 0
r[4] = 10550400
r[5] = 1

main loop
2 seti 1 0 3        r[3] = 1
3 mulr 5 3 4        r[4] = r[5] * r[3]
4 eqrr 4 1 4        r[4] = r[4] == r[1]
5 addr 4 2 2        r[2] = r[4] + r[2]  #jump, goto 6 or 7
6 addi 2 1 2        r[2] = r[2] + 1     #jump, goto 8
7 addr 5 0 0        r[0] = r[5] + r[0]
8 addi 3 1 3        r[3] = r[3] + 1
9 gtrr 3 1 4        r[4] = r[3] > r[1]
10 addr 2 4 2       r[2] = r[2] + r[4]  #jump, goto 11 or 12
11 seti 2 1 2       r[2] = 2            #jump, goto 3
12 addi 5 1 5       r[5] = r[5] + 1
13 gtrr 5 1 4       r[4] = r[5] > r[1]
14 addr 4 2 2       r[2] = r[4] + r[2]  #jump, goto 15 or 16
15 seti 1 1 2       r[2] = 1            #jump, goto 2
16 mulr 2 2 2       r[2] = r[2] * r[2]  #jump, exit

==>

r[0] = 0
r[1] = 10551292
r[2] = 1
r[3] = 0
r[4] = 10550400
r[5] = 1

while r[5] <= r[1]:         #line 13-16
    r[3] = 1
    while r[3] <= r[1]:     #line 9-10
        r[4] = r[5] * r[3]
        if r[4] == r[1]:    #line 4-5
            r[0] += r[5]
        r[3] += 1
    r[5] += 1

simplified ==>

r[0] = 0
r[1] = 10551292
r[5] = 1
while r[5] <= r[1]:
    r[3] = 1
    while r[3] <= r[1]:
        if r[5] * r[3] == r[1]:
            r[0] += r[5]
        r[3] += 1
    r[5] += 1

==>
this adds up all divisors of 10551292
'''

# too slow, not in use anymore
def f():
    while registers[ip_reg] < len(instructions):
        l = instructions[registers[ip_reg]]
        op, a, b, c = l.split(" ")
        globals()[op](int(a), int(b), int(c))
        registers[ip_reg] += 1
    return registers[0]


def all_divisors(n):
    out = []
    for i in range(1, n + 1):
        if n % i == 0:
            out.append(i)
    return out


registers = defaultdict(int)
ip_reg = int(lines[0][-1])
instructions = lines[1:]
#p1 = f() # can be replaced with the faster approach of part 2:
p1 = sum(all_divisors(892))

p2 = sum(all_divisors(10551292))

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
