import re

with open('input.txt') as file:
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in file]


def in_range(p, q):
    d = 0
    for i in range(4):
        d += abs(p[i] - q[i])
    return d <= 3


con = []
for p in intlines:
    merged = [p]
    for c in con:
        for q in c:
            if in_range(p, q):
                merged = merged + c
                con.remove(c)
                break
    con.append(merged)

p1 = len(con)
print("Part 1: " + str(p1))
