from queue import LifoQueue

with open("advent_9.txt") as f:
  lines = [line.strip() for line in f.readlines()]

x = len(lines[0])
y = len(lines)

board = [[-1 for i in range(x)] for j in range(y)]

for j, line in enumerate(lines):
  for i, p in enumerate(line):
    board[j][i] = int(p)


class Position(object):
  def __init__(self, i, j):
    self.i = i
    self.j = j

  def compare(self, other):
    if other.i >= 0 and other.j >= 0 and other.i < x and other.j < y:
      if board[self.j][self.i] < board[other.j][other.i]:
        return -1
      elif board[self.j][self.i] == board[other.j][other.i]:
        return 0
      else:
        return 1

  def get_index(self):
    return 1000 * self.j + self.i


to_low = dict()


def get_position(index):
  return Position(index % 1000, int(index / 1000))


class Visited(object):
  def __init__(self, position, visited):
    self.position = position
    self.visited = visited

# DFS for low point. Record path. Once low point found,
# update all elements on path.
def find_low(position):
  stack = LifoQueue(maxsize=0)
  stack.put(Visited(position, []))
  while not stack.empty():
    v = stack.get()
    p = v.position
    visited = v.visited + [p]
    neighbors = [Position(p.i-1, p.j), Position(p.i+1, p.j), Position(p.i, p.j-1), Position(p.i, p.j+1)]
    low = True
    for n in neighbors:
      c = p.compare(n)
      if c == 1:
        stack.put(Visited(n, visited))
        low = False
      elif c == 0:
        low = False
    if low:
      for path_p in visited:
        to_low[path_p.get_index()] = p


total = 0
for j in range(y):
  for i in range(x):
    p = Position(i, j)
    if board[j][i] < 9 and (p.get_index() not in to_low):
      find_low(p)

sizes = {}
for p in to_low:
  ind = to_low[p].get_index()
  if ind not in sizes:
    sizes[ind] = 1
  else:
    sizes[ind] += 1

size_arr = [v for v in sizes.values()]
size_arr.sort(reverse=True)
print(size_arr[0]*size_arr[1]*size_arr[2])
