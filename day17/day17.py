import re

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def all_ints_in_string(s):
    return [int(n) for n in re.findall(r'-?\d+', s)]


def fall(p):
    x, y = p
    while (x, y + 1) not in clay and (x, y + 1) not in reservoir:
        y += 1
        reachable.add((x, y))
        if y > max_y:
            return
    r = flow((x, y), 1)
    l = flow((x, y), -1)
    if r is not None and l is not None:
        reservoir.update(l)
        reservoir.update(r)


def flow(p, dx):
    x, y = p
    path = set()
    path.add((x, y))
    while (x + dx, y) not in clay and ((x, y + 1) in clay or (x, y + 1) in reservoir):
        x += dx
        reachable.add((x, y))
        path.add((x, y))
    if (x, y + 1) not in clay and (x, y + 1) not in reservoir:
        fall((x, y))
    else:
        return path


clay = set()
reachable = set()
reservoir = set()
for l in lines:
    ints = all_ints_in_string(l)
    if l.startswith("x"):
        x = ints[0]
        for y in range(ints[1], ints[2] + 1):
            clay.add((x, y))
    else:
        y = ints[0]
        for x in range(ints[1], ints[2] + 1):
            clay.add((x, y))

min_y = min([p[1] for p in clay])
max_y = max([p[1] for p in clay])

spring = (500, 0)
reachable.add(spring)
while max_y >= max([p[1] for p in reachable]):
    fall(spring)

p1 = 0
for x, y in reachable:
    if min_y <= y <= max_y:
        p1 += 1
p2 = len(reservoir)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
