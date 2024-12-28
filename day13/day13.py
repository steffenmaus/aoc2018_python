with open('input.txt') as file:
    lines = [line.rstrip() for line in file]

p1 = 0
p2 = 0

carts = {}

maze = {}
for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        p = (x, y)
        c = lines[y][x]
        match c:
            case "-":
                maze[p] = "-"
            case "|":
                maze[p] = "|"
            case "\\":
                maze[p] = "\\"
            case "/":
                maze[p] = "/"
            case "+":
                maze[p] = "+"
            case "v":
                maze[p] = "|"
                carts[p] = ("v", "L")
            case "<":
                maze[p] = "-"
                carts[p] = ("<", "L")
            case ">":
                maze[p] = "-"
                carts[p] = (">", "L")
            case "^":
                maze[p] = "|"
                carts[p] = ("^", "L")

turnings = {}
turnings["L^"] = "<"
turnings["Lv"] = ">"
turnings["L<"] = "v"
turnings["L>"] = "^"
turnings["R^"] = ">"
turnings["Rv"] = "<"
turnings["R<"] = "^"
turnings["R>"] = "v"
turnings["S^"] = "^"
turnings["Sv"] = "v"
turnings["S<"] = "<"
turnings["S>"] = ">"


def make_step(p, cart):
    dir, turn = cart
    x, y = p

    match dir:
        case "^":
            p_next = (x, y - 1)
        case "v":
            p_next = (x, y + 1)
        case ">":
            p_next = (x + 1, y)
        case "<":
            p_next = (x - 1, y)

    dir_next = dir
    turn_next = turn
    match maze[p_next]:
        case "+":
            dir_next = turnings[turn + dir]
            match turn:
                case "L":
                    turn_next = "S"
                case "S":
                    turn_next = "R"
                case "R":
                    turn_next = "L"
        case "/":
            match dir:
                case "^":
                    dir_next = ">"
                case "v":
                    dir_next = "<"
                case "<":
                    dir_next = "v"
                case ">":
                    dir_next = "^"
        case "\\":
            match dir:
                case "^":
                    dir_next = "<"
                case "v":
                    dir_next = ">"
                case "<":
                    dir_next = "^"
                case ">":
                    dir_next = "v"

    return p_next, dir_next, turn_next


p1 = None
p2 = None
while len(carts) > 1:
    for next_pos in sorted(carts.keys()):
        if next_pos in carts.keys() and len(carts) > 1:
            next = make_step(next_pos, carts.pop(next_pos))
            if next[0] in carts.keys():
                if p1 is None:
                    p1 = str(next[0][0]) + "," + str(next[0][1])
                carts.pop(next[0])
            else:
                carts[next[0]] = next[1], next[2]

last_cart = list(carts.keys())[0]
p2 = str(last_cart[0]) + "," + str(last_cart[1])

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
