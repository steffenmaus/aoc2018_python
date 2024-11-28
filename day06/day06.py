import sys

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def total_distance_is_below(p, threshold):  # shortcut
    total = 0
    for i, _ in enumerate(nodes):
        n = nodes[i]
        d = abs(n[0] - p[0]) + abs(n[1] - p[1])
        total += d
        if total >= threshold:
            return False
    return total < threshold


def get_closest(p):
    dist = sys.maxsize
    closest = None
    for i, _ in enumerate(nodes):
        n = nodes[i]
        d = abs(n[0] - p[0]) + abs(n[1] - p[1])
        if d < dist:
            dist = d
            closest = i
        elif d == dist:
            closest = None
    return closest


def get_most():
    count = 0
    for i, _ in enumerate(nodes):
        if i not in infinites:
            c = 0
            for e in closest:
                if closest[e] == i:
                    c += 1
            if c > count:
                count = c
    return count


nodes = []
closest = {}
infinites = set()

for l in lines:
    x, y = l.split(', ')
    nodes.append((int(x), int(y)))

min_x = min([p[0] for p in nodes])
max_x = max([p[0] for p in nodes])
min_y = min([p[1] for p in nodes])
max_y = max([p[1] for p in nodes])

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        p = (x, y)
        closest[p] = get_closest(p)
        if x == min_x or x == max_x or y == min_y or y == max_y and closest[p]:
            infinites.add(closest[p])

p1 = get_most()

print("Part 1: " + str(p1))

p2 = 0
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        if total_distance_is_below((x, y), 10000):
            p2 += 1

print("Part 2: " + str(p2))
