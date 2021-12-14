sub = dict()

with open("advent_14.txt") as f:
  poly_input = f.readline().strip()
  f.readline()
  for line in f.readlines():
    source, insert = line.strip().split("->")
    sub[source.strip()] = insert.strip()

class Node(object):
  def __init__(self, name, next_node=None):
    self.name = name
    self.next_node = next_node

  def insert(self, new_node):
    new_node.next_node = self.next_node
    self.next_node = new_node

head = Node(poly_input[0])
current = head
for c in poly_input[1:]:
  new_node = Node(c)
  current.insert(new_node)
  current = new_node

for i in range(10):
  current = head
  while current.next_node is not None:
    next_node = current.next_node
    key = current.name + next_node.name
    if key in sub:
      current.insert(Node(sub[key]))
    current = next_node

current = head
out = []
while current is not None:
  out.append(current.name)
  current = current.next_node

counts = dict()
for el in out:
  if el not in counts:
    counts[el] = 1
  else:
    counts[el] += 1

max_o = max(counts.values())
min_o = min(counts.values())
print(max_o - min_o)
