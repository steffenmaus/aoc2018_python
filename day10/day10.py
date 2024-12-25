import re
import sys

with open('input.txt') as file:
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in file]


def draw_points(points):
    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])
    for y in range(min_y, max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in points:
                line += "█"
            else:
                line += " "
        print(line)


p2 = None
last_y_range = sys.maxsize
last_horizon = None
time = 0
print("Part 1: ")
while p2 is None:
    time += 1
    horizon = set()
    for x, y, dx, dy in intlines:
        x = x + dx * time
        y = y + dy * time
        horizon.add((x, y))
    y_range = max([p[1] for p in horizon]) - min([p[1] for p in horizon])
    if y_range > last_y_range:
        draw_points(last_horizon)
        repeat = False
        p2 = time - 1
    last_y_range = y_range
    last_horizon = horizon

print("Part 2: " + str(p2))
