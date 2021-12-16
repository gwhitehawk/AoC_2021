from operator import itemgetter


with open("advent_15.txt") as f:
  init_board = [[int(el) for el in line.strip()] for line in f.readlines()]

def mod_9(num):
  m = num % 9
  if m == 0:
    return 9
  return m

init_size = len(init_board)
size = 5 * init_size
board = [[-1 for i in range(size)] for j in range(size)]

for j in range(5):
  for i in range(5):
    for y in range(init_size):
      for x in range(init_size):
        board[j * init_size + y][i * init_size + x] = mod_9(init_board[y][x] + j + i)

min_risk = [20*size for i in range(size*size)]
min_risk[0] = 0


class Position(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return ("({}, {})".format(self.x, self.y))

  def get_neighbors(self):
    x, y = self.x, self.y
    neighbors = []
    for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
      if i >=0 and i < size and j >= 0 and j < size:
        neighbors.append(Position(i, j))
    return neighbors

  def get_index(self):
    return size*self.y + self.x


class Path(object):
  def __init__(self, current, cost=0):
    self.current = current
    self.cost = cost


def get_position(i):
  return Position(i % size, int(i / size))

unvisited = set([i for i in range(size*size)])

while (size * size - 1) in unvisited:
  current_index, _ = min({i: min_risk[i] for i in unvisited}.items(), key=itemgetter(1))
  current_pos = get_position(current_index)
  # print("current: {}".format(current_pos.__str__()))

  for n in current_pos.get_neighbors():
    n_index = n.get_index()
    if n_index in unvisited:
      new_cost = min_risk[current_index] + board[n.y][n.x]
      if new_cost < min_risk[n_index]:
        min_risk[n_index] = new_cost
  unvisited.remove(current_index)

print(min_risk[size*size-1])
