import re
from collections import defaultdict

with open('input.txt') as file:
    intlines = [[int(n) for n in re.findall(r'-?\d+', line)] for line in file]


class Marble:
    def __init__(self, n):
        self.n = n

    def get_value(self):
        return self.n

    def get_clockwise(self):
        return self.clockwise

    def get_counterclockwise(self):
        return self.counterclockwise

    def set_clockwise(self, marble):
        self.clockwise = marble

    def set_counterclockwise(self, marble):
        self.counterclockwise = marble

    def add_clockwise(self, marble):
        marble.set_counterclockwise(self)
        marble.set_clockwise(self.get_clockwise())

        self.get_clockwise().set_counterclockwise(marble)
        self.set_clockwise(marble)

    def remove_counterclockwise(self):
        marble = self.get_counterclockwise()
        self.set_counterclockwise(marble.get_counterclockwise())
        marble.get_counterclockwise().set_clockwise(self)
        return marble


players, last_marble = intlines[0]

init = Marble(0)
current = init
current.set_clockwise(current)
current.set_counterclockwise(current)

scores = defaultdict(int)

for i in range(1, 100 * last_marble + 1):
    if i == last_marble + 2:
        p1 = max(scores.values())
    if i % 23 == 0:
        scores[i % players] += i
        for _ in range(6):
            current = current.get_counterclockwise()
        scores[i % players] += current.remove_counterclockwise().get_value()
    else:
        new_marble = Marble(i)
        current.get_clockwise().add_clockwise(new_marble)
        current = new_marble

p2 = max(scores.values())
print("Part 1: " + str(p1))
print("Part 2: " + str(p2))
