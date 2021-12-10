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


def compare_positions(p1, p2):
  if p2.i >= 0 and p2.j >= 0 and p2.i < x and p2.j < y:
    if board[p1.j][p1.i] < board[p2.j][p2.i]:
      return -1
    elif board[p1.j][p1.i] == board[p2.j][p2.i]:
      return 0
    else:
      return 1

  return -1


to_low = dict()


def make_index(p):
  return 1000*p.j + p.i


def get_position(index):
  return Position(index % 1000, int(index / 1000))


class Visited(object):
  def __init__(self, position, visited):
    self.position = position
    self.visited = visited

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
      c = compare_positions(p, n)
      if c == 1:
        stack.put(Visited(n, visited))
        low = False
      elif c == 0:
        low = False
    if low:
      for path_p in visited:
        to_low[make_index(path_p)] = p


total = 0
for j in range(y):
  for i in range(x):
    p = Position(i, j)
    if board[j][i] < 9 and (make_index(p) not in to_low):
      find_low(p)

sizes = {}
for p in to_low:
  ind = make_index(to_low[p])
  if ind not in sizes:
    sizes[ind] = 1
  else:
    sizes[ind] += 1

size_arr = [v for v in sizes.values()]
size_arr.sort(reverse=True)
print(size_arr[0]*size_arr[1]*size_arr[2])
