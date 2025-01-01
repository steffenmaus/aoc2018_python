import heapq
import re
from collections import defaultdict

with open('input.txt') as file:
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in file]


def get_all_nei_2d_4(p):
    x, y = p
    r = [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]
    return r


def dijkstra(start, target, distances):
    out = {}
    out[start] = 0
    Q = []
    for nei in distances[start]:
        node, dist = nei
        heapq.heappush(Q, (dist, node, start))
    while target not in out:
        dist, current, prev = heapq.heappop(Q)
        if current not in out.keys():
            out[current] = dist
            for nei in distances[current]:
                n, d = nei
                heapq.heappush(Q, (d + dist, n, current))
    return out[target]


def get_distances():
    distances = defaultdict(list)
    for y in range(Y):
        for x in range(X):
            for item in (0, 1, 2):
                p = (x, y, item)
                match get_erosion_lvl((x, y)) % 3:
                    case 0:
                        distances[p].append(((x, y, 1), 7))
                        distances[p].append(((x, y, 2), 7))
                    case 1:
                        distances[p].append(((x, y, 0), 7))
                        distances[p].append(((x, y, 2), 7))
                    case 2:
                        distances[p].append(((x, y, 0), 7))
                        distances[p].append(((x, y, 1), 7))

                for n in get_all_nei_2d_4((x, y)):
                    if n in geologic.keys():
                        q = (n[0], n[1], item)
                        er_n = get_erosion_lvl(n) % 3
                        if item == 0 and er_n in (1, 2):
                            distances[p].append((q, 1))
                        if item == 1 and er_n in (0, 2):
                            distances[p].append((q, 1))
                        if item == 2 and er_n in (0, 1):
                            distances[p].append((q, 1))

    return distances


def get_erosion_lvl(p):
    return (geologic[p] + depth) % 20183


p1 = 0

start = (0, 0)
depth = intlines[0][0]
target = intlines[1][0], intlines[1][1]
geologic = {}
geologic[start] = 0
geologic[target] = 0
X = 2 * target[0]  # might be too small
Y = 2 * target[1]  # might be too small
for y in range(Y):
    for x in range(X):
        p = (x, y)
        if p not in geologic:
            if y == 0:
                geologic[p] = x * 16807
            elif x == 0:
                geologic[p] = y * 48271
            else:
                geologic[p] = get_erosion_lvl((x - 1, y)) * get_erosion_lvl((x, y - 1))
        if x <= target[0] and y <= target[1]:
            p1 += get_erosion_lvl(p) % 3

# 0: none
# 1: torch
# 2: climb
distances = get_distances()

p2 = dijkstra((start[0], start[1], 1), (target[0], target[1], 1), distances)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
