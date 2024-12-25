with open('input.txt') as file:
    lines = [line.rstrip() for line in file]


def parse_node(pos):
    q_child_nodes = definitions[pos]
    q_meta_entries = definitions[pos + 1]
    childs = []
    metas = []
    pos += 2
    for _ in range(q_child_nodes):
        c, pos = parse_node(pos)
        childs.append(c)
    for _ in range(q_meta_entries):
        metas.append(definitions[pos])
        pos += 1
    return (childs, metas), pos


def sum_of_metas(node):
    out = sum(node[1])
    for c in node[0]:
        out += sum_of_metas(c)
    return out


def calc_value(node):
    childs, metas = node
    if childs:
        out = 0
        for m in metas:
            m = m - 1
            if 0 <= m < len(childs):
                out += calc_value(childs[m])
        return out
    else:
        return sum(metas)


definitions = list(map(int, lines[0].split()))

root = parse_node(0)[0]

p1 = sum_of_metas(root)
p2 = calc_value(root)

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
