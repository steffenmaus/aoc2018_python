class Recipe:
    def __init__(self, n):
        self.n = n

    def get_value(self):
        return self.n

    def get_clockwise(self):
        return self.clockwise

    def set_clockwise(self, recipe):
        self.clockwise = recipe

    def add_clockwise(self, recipe):
        recipe.set_clockwise(self.get_clockwise())
        self.set_clockwise(recipe)


puzzle_input = 540391
target = [int(x) for x in list(str(puzzle_input))]

a = Recipe(3)
b = Recipe(7)
a.set_clockwise(b)
b.set_clockwise(a)
elf_one = a
elf_two = b
last_item = b

total = 2

recent_recipes = []
recent_recipes.append(3)
recent_recipes.append(7)
p1 = None
p2 = None

while p1 is None or p2 is None:
    recent_recipes = recent_recipes[-10:]
    sum = elf_one.get_value() + elf_two.get_value()
    if sum > 9:
        r = Recipe(1)
        recent_recipes.append(1)
        last_item.add_clockwise(r)
        last_item = r
        total += 1
        if p1 is None and total == puzzle_input + 10:
            p1 = "".join(str(x) for x in recent_recipes[-10:])
        if p2 is None and recent_recipes[-6:] == target:
            p2 = total - 6

    r = Recipe(sum % 10)
    recent_recipes.append(sum % 10)
    last_item.add_clockwise(r)
    last_item = r
    total += 1
    if p1 is None and total == puzzle_input + 10:
        p1 = "".join(str(x) for x in recent_recipes[-10:])
    if p2 is None and recent_recipes[-6:] == target:
        p2 = total - 6

    for _ in range(1 + elf_one.get_value()):
        elf_one = elf_one.get_clockwise()
    for _ in range(1 + elf_two.get_value()):
        elf_two = elf_two.get_clockwise()

print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
