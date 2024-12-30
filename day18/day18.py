with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def get_all_nei_2d_8(p):
    x, y = p
    out = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx != 0 or dy != 0:
                out.append((x + dx, y + dy))
    return out


def calc_score(maze):
    lumb = 0
    wood = 0
    for p in maze:
        lumb += maze[p] == "#"
        wood += maze[p] == "|"
    return lumb * wood


def get_state_of_maze(maze):
    state = ""
    for y in range(0, Y):
        for x in range(0, X):
            state += maze[(x, y)]
    return state


def f(maze, times):
    states = {}
    scores = {}
    for time in range(times):
        scores[time] = calc_score(maze)
        state = get_state_of_maze(maze)
        if state in states.keys():
            cycle = time - states[state]
            remaining = times - time
            return scores[states[state] + (remaining % cycle)]
        else:
            states[state] = time
        next_maze = {}
        for y in range(0, Y):
            for x in range(0, X):
                p = (x, y)
                n = [maze[q] for q in get_all_nei_2d_8(p) if q in maze.keys()]
                match maze[p]:
                    case ".":
                        if n.count("|") >= 3:
                            next_maze[p] = "|"
                        else:
                            next_maze[p] = "."
                    case "|":
                        if n.count("#") >= 3:
                            next_maze[p] = "#"
                        else:
                            next_maze[p] = "|"
                    case "#":
                        if n.count("#") >= 1 and n.count("|") >= 1:
                            next_maze[p] = "#"
                        else:
                            next_maze[p] = "."
        maze = next_maze
    return calc_score(maze)


X = len(lines[0])
Y = len(lines)

maze = {}
for y in range(0, Y):
    for x in range(0, X):
        p = (x, y)
        c = lines[y][x]
        maze[p] = c

p1 = f(maze.copy(), 10)
p2 = f(maze.copy(), 1000000000)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
