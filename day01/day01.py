with open('input.txt') as file:
    lines = [int(line.rstrip()) for line in file]

mem = set()
freq = 0
p1 = None
p2 = None
while p2 is None:
    for l in lines:
        if freq in mem and p2 is None:
            p2 = freq
        mem.add(freq)
        freq += l
    if p1 is None:
        p1 = freq

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
