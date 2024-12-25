serial_number = 9995

X, Y = 300, 300
power_levels = {}
for y in range(1, Y + 1):
    for x in range(1, X + 1):
        rack_id = x + 10
        power_level = rack_id * y
        power_level += serial_number
        power_level *= rack_id
        power_level = (power_level // 100) % 10
        power_level -= 5
        power_levels[(x, y)] = power_level

partial_sums = {}
for y in range(1, Y + 1):
    for x in range(1, X + 1):
        if x == y == 1:
            partial_sums[(x, y)] = power_levels[(x, y)]
        elif x == 1:
            partial_sums[(x, y)] = power_levels[(x, y)] + partial_sums[(x, y - 1)]
        elif y == 1:
            partial_sums[(x, y)] = power_levels[(x, y)] + partial_sums[(x - 1, y)]
        else:
            partial_sums[(x, y)] = power_levels[(x, y)] + partial_sums[(x - 1, y)] + partial_sums[(x, y - 1)] - \
                                   partial_sums[(x - 1, y - 1)]

best_p1 = 0
best_p2 = 0

for y in range(1, Y + 1):
    for x in range(1, X + 1):
        for w in range(1, X + 1 - max(x, y)):
            if x == y == 1:
                total = partial_sums[(x + w - 1, y + w - 1)]
            elif x == 1:
                total = partial_sums[(x + w - 1, y + w - 1)] - partial_sums[(x + w - 1, y - 1)]
            elif y == 1:
                total = partial_sums[(x + w - 1, y + w - 1)] - partial_sums[(x - 1, y + w - 1)]
            else:
                total = partial_sums[(x + w - 1, y + w - 1)] - partial_sums[(x + w - 1, y - 1)] - \
                        partial_sums[(x - 1, y + w - 1)] + partial_sums[(x - 1, y - 1)]

            if w == 3 and total > best_p1:
                p1 = str(x) + "," + str(y)
                best_p1 = total
            if total > best_p2:
                p2 = str(x) + "," + str(y) + "," + str(w)
                best_p2 = total

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
