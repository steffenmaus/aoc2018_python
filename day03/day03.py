with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

squares = {}

in_use = set()
overlap = set()

for l in lines:
    x = int(l.split()[2].split(",")[0])
    y = int(l.split()[2].split(",")[1][:-1])
    w = int(l.split()[3].split("x")[0])
    h = int(l.split()[3].split("x")[1])
    squares[int(l.split()[0][1:])] = (x, y, w, h)

for k, s in squares.items():
    for x in range(s[0], s[0] + s[2]):
        for y in range(s[1], s[1] + s[3]):
            if (x, y) in in_use:
                overlap.add((x, y))
            in_use.add((x, y))

p1 = len(overlap)
p2 = None

for k, s in squares.items():
    perfect = True
    for x in range(s[0], s[0] + s[2]):
        for y in range(s[1], s[1] + s[3]):
            if (x, y) in overlap:
                perfect = False
    if perfect:
        p2 = k

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
