import copy
from queue import Queue


with open("advent_12.txt") as f:
  lines = [line.strip() for line in f.readlines()]


class Cave(object):
  def __init__(self, name):
    self.name = name
    self.neighbors = set()

  def __str__(self):
    return "{}: {}".format(self.name, self.neighbors)


caves = dict()


for line in lines:
  line_c = set(line.split("-"))
  for c in line_c:
    if c not in caves:
      caves[c] = Cave(c)
      caves[c].neighbors = line_c.difference(set([c]))
    else:
      caves[c].neighbors.add(line_c.difference(set([c])).pop())


print([cave.__str__() for cave in caves.values()])


class Visited(object):
  def __init__(self, cave, visited):
    self.cave = cave
    self.visited = visited


paths = []
q = Queue(maxsize=0)

q.put(Visited(caves["start"], ["start"]))
while not q.empty():
  current = q.get()
  for n in current.cave.neighbors:
    if n == "end":
      paths.append(current.visited + ["end"])
    elif n.isupper() or n not in current.visited:
      new_visited = copy.deepcopy(current.visited) + [n]
      q.put(Visited(caves[n], new_visited))

print(len(paths))
