import re

with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def all_ints_in_string(s):
    return [int(n) for n in re.findall(r'-?\d+', s)]


def f(boost):
    groups = {}
    for l in lines:
        if l:
            if l == "Immune System:":
                is_immune = True
            elif l == "Infection:":
                is_immune = False
            else:
                count, hp, dmg, initiative = all_ints_in_string(l)
                if is_immune:
                    dmg += boost
                dmg_type = l.split(" damage ")[0].split(" ")[-1]
                weak = []
                immune = []
                if "immune to" in l:
                    x = l.split("immune to ")[1]
                    x = x.split(";")[0].split(")")[0]
                    for i in x.split(", "):
                        immune.append(i)
                if "weak to" in l:
                    x = l.split("weak to ")[1]
                    x = x.split(";")[0].split(")")[0]
                    for i in x.split(", "):
                        weak.append(i)
                groups[initiative] = (is_immune, count, hp, dmg, dmg_type, weak, immune)

    while len(set([g[0] for g in groups.values()])) > 1:
        candidates = []
        for id, group in groups.items():
            candidates.append((id, group[1] * group[3]))
        candidates = sorted(sorted(candidates, reverse=True), key=lambda t: t[1], reverse=True)

        selected = {}
        for c in candidates:
            attacker_id, _ = c
            attacker = groups[attacker_id]
            targets = []
            for target_id, target in groups.items():
                if target_id not in selected.values():
                    if attacker[0] != target[0]:
                        dmg_pred = attacker[1] * attacker[3]
                        if attacker[4] in target[6]:
                            dmg_pred = 0
                        elif attacker[4] in target[5]:
                            dmg_pred *= 2
                        if dmg_pred > 0:
                            targets.append((target_id, dmg_pred, target[1] * target[3]))

            targets = sorted(sorted(sorted(targets, reverse=True), key=lambda t: t[2], reverse=True),
                             key=lambda t: t[1], reverse=True)
            if targets:
                selected[attacker_id] = targets[0][0]

        total_losses = 0
        for id in reversed(sorted(selected.keys())):
            if id in groups.keys():
                group = groups[id]
                target = groups[selected[id]]
                dmg = group[1] * group[3]
                if group[4] in target[6]:
                    dmg = 0
                elif group[4] in target[5]:
                    dmg *= 2
                losses = dmg // target[2]
                total_losses += losses
                if losses >= target[1]:
                    groups.pop(selected[id])
                else:
                    groups[selected[id]] = (
                        target[0], target[1] - losses, target[2], target[3], target[4], target[5], target[6])
        if total_losses == 0:
            return None
    return groups


p1 = 0

for g in f(0).values():
    p1 += g[1]

print("Part 1: " + str(p1))

p2 = 0
boost = 1
while True:
    res = f(boost)
    if res is not None:
        if all([g[0] for g in res.values()]):
            for g in res.values():
                p2 += g[1]
            break
    boost += 1

print("Part 2: " + str(p2))
