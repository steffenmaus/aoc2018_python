with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def duration(c):
    return ord(c) - 4


nodes = set()
requires = {}

for l in lines:
    left = l.split()[1]
    right = l.split()[-3]
    nodes.add(left)
    nodes.add(right)
    if right in requires.keys():
        requires[right].append(left)
    else:
        requires[right] = [left]
    if left not in requires:
        requires[left] = []

completed = set()

p1 = ""

while completed != nodes:
    for n in sorted(list(nodes)):
        if n not in completed:
            if not requires[n]:
                completed.add(n)
                p1 = p1 + n
                for m in nodes:
                    if n in requires[m]:
                        requires[m].remove(n)
                break

print("Part 1: " + str(p1))

for n in nodes:
    requires[n] = []

for l in lines:
    left = l.split()[1]
    right = l.split()[-3]
    requires[right].append(left)

available = set()
completed = set()
in_progress = set()  # (node, until)

for n in nodes:
    if not requires[n]:
        available.add(n)

p2 = -1
while available or in_progress:
    p2 += 1
    dele = []
    for x in in_progress:
        if x[1] == p2:
            dele.append(x)
            for m in nodes:
                if x[0] in requires[m]:
                    requires[m].remove(x[0])
    for d in dele:
        in_progress.remove(d)
    for n in nodes:
        if n not in completed and not requires[n]:
            available.add(n)
    while len(in_progress) < 5 and available:
        temp = min(available)
        available.remove(temp)
        in_progress.add((temp, p2 + duration(temp)))
        completed.add(temp)

print("Part 2: " + str(p2))
