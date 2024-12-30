import heapq
import sys
from collections import defaultdict

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def dijkstra_full(start, distances):
    out = {}
    out[start] = 0
    Q = []
    for nei in distances[start]:
        node, dist = nei
        heapq.heappush(Q, (dist, node, start))
    while len(out.keys()) != len(distances.keys()):
        dist, current, prev = heapq.heappop(Q)
        if current not in out.keys():
            out[current] = dist
            for nei in distances[current]:
                n, d = nei
                heapq.heappush(Q, (d + dist, n, current))
    return out


mem = set()


def f(p, pointer):
    if (p, pointer) in mem:
        return
    mem.add((p, pointer))
    x, y = p
    floor.add(p)
    match input[pointer]:
        case "$":
            return
        case "N":
            q = (x, y - 1)
            distances[p].append((q, 1))
            distances[q].append((p, 1))
            f(q, pointer + 1)
        case "E":
            q = (x + 1, y)
            distances[p].append((q, 1))
            distances[q].append((p, 1))
            f(q, pointer + 1)
        case "S":
            q = (x, y + 1)
            distances[p].append((q, 1))
            distances[q].append((p, 1))
            f(q, pointer + 1)
        case "W":
            q = (x - 1, y)
            distances[p].append((q, 1))
            distances[q].append((p, 1))
            f(q, pointer + 1)
        case "(":
            for s in all_options[pointer]:
                f(p, s)
        case ")":
            f(p, pointer + 1)
        case "|":
            f(p, to_closure[pointer])


floor = set()
distances = defaultdict(list)
start = (0, 0)
input = lines[0][1:]

all_options = defaultdict(list)
to_closure = {}
open_stack = []
for i in range(len(input)):
    match input[i]:
        case "(":
            open_stack.append(i)
            all_options[i].append(i + 1)
        case "|":
            all_options[open_stack[-1]].append(i + 1)
        case ")":
            for c in all_options[open_stack[-1]]:
                to_closure[c - 1] = i
            to_closure[open_stack.pop()] = i

sys.setrecursionlimit(10000)
f(start, 0)

res = dijkstra_full(start, distances)

p1 = max(res.values())
p2 = len([x for x in res.values() if x >= 1000])

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
