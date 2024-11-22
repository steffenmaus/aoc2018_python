with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

asleep = set()
guards = set()

felt_asleep_t = None
guard = None

for l in sorted(lines):
    day = l.split()[0]
    minute = int(l.split()[1][3:5])
    if "begins shift" in l:
        guard = int(l.split()[3][1:])
        guards.add(guard)
    elif "falls asleep" in l:
        felt_asleep_t = minute
    elif "wakes up" in l:
        for t in range(felt_asleep_t, minute):
            asleep.add((guard, day, t))

most_sleepy_guard = None
highest_sleep_duration = 0

for g in guards:
    total = 0
    for a in asleep:
        if a[0] == g:
            total += 1
    if total > highest_sleep_duration:
        highest_sleep_duration = total
        most_sleepy_guard = g

crucial_minute = None
amount_naps = 0

for t in range(0, 60):
    total = 0
    for a in asleep:
        if a[0] == most_sleepy_guard and a[2] == t:
            total += 1
    if total > amount_naps:
        crucial_minute = t
        amount_naps = total

p1 = most_sleepy_guard * crucial_minute
print("Part 1: " + str(p1))

p2_time = None
p2_guard = None
p2_count = 0
for g in guards:
    for t in range(0, 60):
        total = 0
        for a in asleep:
            if a[0] == g and a[2] == t:
                total += 1
        if total > p2_count:
            p2_time = t
            p2_count = total
            p2_guard = g

p2 = p2_guard * p2_time
print("Part 2: " + str(p2))
