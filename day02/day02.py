with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

overall_two = 0
overall_three = 0

for l in lines:
    two = False
    three = False
    for c in l:
        match l.count(c):
            case 2:
                two = True
            case 3:
                three = True
    overall_two += two
    overall_three += three

p1 = overall_two * overall_three
print("Part 1: " + str(p1))

p2 = None
for a in lines:
    for b in lines:
        if a != b:
            for i, _ in enumerate(a):
                short_a = a[:i] + a[i + 1:]
                short_b = b[:i] + b[i + 1:]
                if short_a == short_b:
                    p2 = short_a
                    break

print("Part 2: " + str(p2))
