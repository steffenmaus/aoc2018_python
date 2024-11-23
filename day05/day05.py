import string
import sys

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def f(polymer):
    res = []
    for i, v in enumerate(polymer):
        if res and res[-1].lower() == v.lower() and res[-1] != v:
            res.pop()
        else:
            res.append(v)
    return res


p1 = len(f(lines[0]))
p2 = sys.maxsize

for c in string.ascii_lowercase:
    current = [x for x in lines[0] if x.lower() != c]
    p2 = min(p2, len(f(current)))

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
