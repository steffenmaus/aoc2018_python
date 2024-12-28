with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def calc_score(start_pos, current):
    score = 0
    for c in current:
        score += start_pos * (c == "#")
        start_pos += 1
    return score


current = lines[0].split()[-1]

start_pos = 0

mappings = {}
for l in lines[2:]:
    l, r = l.split(" => ")
    mappings[l] = r

mem = {}

for t in range(50000000000):
    current = "..." + current + "..."
    next = ""
    for i in range(len(current) - 4):
        next += mappings[current[i:i + 5]]
    start_pos -= 1
    current = next
    while current.startswith("."):
        current = current[1:]
        start_pos += 1
    while current.endswith("."):
        current = current[:-1]
    if t == 19:
        p1 = calc_score(start_pos, current)
    if current in mem.keys():
        delta_pos = start_pos - mem[current]
        p2 = calc_score(start_pos + (50000000000 - 1 - t) * delta_pos, current)

        break
    else:
        mem[current] = start_pos

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
