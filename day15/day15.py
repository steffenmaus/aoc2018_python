with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei_2d_4(p):
    x, y = p
    r = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]
    return r


def get_sorted_by_reading_order(points):
    return sorted(sorted(points), key=lambda t: t[1])


def get_nearest_reachable(floor, start, targets):
    border = set()
    completed = set()
    border.add(start)
    while border:
        if border.intersection(targets):
            return get_sorted_by_reading_order(border.intersection(targets))[0]
        new_border = set()
        while border:
            current = border.pop()
            completed.add(current)
            for n in get_all_nei_2d_4(current):
                if n in floor and n not in completed:
                    new_border.add(n)
        border = new_border
    return None


def combat(floor, elfs, goblins, elf_dmg):
    initial_elfs = len(elfs)
    rounds = 0
    while elfs.keys() and goblins.keys():
        for p in get_sorted_by_reading_order(set(elfs.keys()).union(goblins.keys())):
            if p in elfs.keys() or p in goblins.keys():
                # move
                allies = elfs
                enemys = goblins
                dmg = elf_dmg
                if p in goblins.keys():
                    allies = goblins
                    enemys = elfs
                    dmg = 3
                all_targets = enemys.keys()
                if not all_targets:
                    break
                reachable_points = set()
                for t in all_targets:
                    for n in get_all_nei_2d_4(t):
                        reachable_points.add(n)
                if p not in reachable_points:
                    reachable_points.difference_update(set(elfs.keys()).union(goblins.keys()))
                    if reachable_points:
                        current_floor = floor.difference(set(elfs.keys()).union(goblins.keys()))
                        res = get_nearest_reachable(current_floor, p, reachable_points)
                        if res:
                            p_new = get_nearest_reachable(current_floor, res, get_all_nei_2d_4(p))
                            allies[p_new] = allies.pop(p)
                            p = p_new
                # attack
                cands = set(get_all_nei_2d_4(p)).intersection(enemys.keys())
                if cands:
                    fewest_hitpoints = min([enemys[p] for p in cands])
                    target = get_sorted_by_reading_order([p for p in cands if enemys[p] == fewest_hitpoints])[0]
                    enemys[target] -= dmg
                    if enemys[target] <= 0:
                        enemys.pop(target)

        rounds += 1
    score = (rounds - 1) * (sum(goblins.values()) + sum(elfs.values()))
    final_elfs = len(elfs)
    return score, final_elfs == initial_elfs


X = len(lines[0])
Y = len(lines)

goblins = {}
elfs = {}
floor = set()
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        match lines[y][x]:
            case "#":
                None
            case ".":
                floor.add(p)
            case "G":
                goblins[p] = 200
                floor.add(p)
            case "E":
                elfs[p] = 200
                floor.add(p)

p1 = combat(floor, elfs.copy(), goblins.copy(), 3)[0]
p2 = None
dmg = 4
while p2 is None:
    res = combat(floor, elfs.copy(), goblins.copy(), dmg)
    if res[1]:
        p2 = res[0]
    dmg += 1

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
