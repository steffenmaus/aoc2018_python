import heapq

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

bots = []

for l in lines:
    x, y, z = [int(i) for i in l.split('<')[1].split('>')[0].split(',')]
    r = int(l.split('=')[2])
    bots.append((x, y, z, r))

max_r = max(b[3] for b in bots)
p1 = 0
for bot in bots:
    x, y, z, r = bot
    if r == max_r:
        for bot2 in bots:
            x2, y2, z2, r2 = bot2
            d = abs(x - x2) + abs(y - y2) + abs(z - z2)
            if d <= r:
                p1 += 1

print("Part 1: " + str(p1))


def bb_is_leaf(bb):
    return bb[0] == bb[1]


def bb_get_childs(bb):
    out = []
    xcut = (bb[1][0] + bb[0][0]) // 2
    ycut = (bb[1][1] + bb[0][1]) // 2
    zcut = (bb[1][2] + bb[0][2]) // 2
    xs = [(bb[0][0], xcut), (xcut + 1, bb[1][0])]
    ys = [(bb[0][1], ycut), (ycut + 1, bb[1][1])]
    zs = [(bb[0][2], zcut), (zcut + 1, bb[1][2])]
    for x in xs:
        for y in ys:
            for z in zs:
                out.append(((x[0], y[0], z[0]), (x[1], y[1], z[1])))
    return out


def bb_get_potential(bb):
    p = 0
    for b in bots:
        if is_in_range_bb_p(bb, b):
            p += 1
    return p


def is_in_range_bb_p(bb, bot):
    x, y, z, r = bot
    d = 0
    if x > bb[1][0]:
        d += abs(x - bb[1][0])
    elif x < bb[0][0]:
        d += abs(bb[0][0] - x)
    if y > bb[1][1]:
        d += abs(y - bb[1][1])
    elif y < bb[0][1]:
        d += abs(bb[0][1] - y)
    if z > bb[1][2]:
        d += abs(z - bb[1][2])
    elif z < bb[0][2]:
        d += abs(bb[0][2] - z)
    return d <= r


min_x, max_x, min_y, max_y, min_z, max_z = 0, 0, 0, 0, 0, 0
for b in bots:
    min_x = min(min_x, b[0])
    max_x = max(max_x, b[0])
    min_y = min(min_y, b[1])
    max_y = max(max_y, b[1])
    min_z = min(min_z, b[2])
    max_z = max(max_z, b[2])
seed = ((min_x, min_y, min_z), (max_x, max_y, max_z))

Q = []
candidates = []
optimum = None
heapq.heappush(Q, (-bb_get_potential(seed), seed))
while True:
    pot_neg, bb = heapq.heappop(Q)
    if optimum is not None and optimum > -pot_neg:
        break
    if bb_is_leaf(bb):
        if optimum is None:
            optimum = -pot_neg
        candidates.append(bb[0])
    else:
        for c in bb_get_childs(bb):
            heapq.heappush(Q, (-bb_get_potential(c), c))

p2 = min([abs(c[0]) + abs(c[1]) + abs(c[2]) for c in candidates])

print("Part 2: " + str(p2))
