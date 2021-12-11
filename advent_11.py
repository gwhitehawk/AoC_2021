def get_index(i, j):
  return 10*j + i

board = [[-1 for i in range(10)] for j in range(10)]

with open("advent_11.txt") as f:
  for j, line in enumerate(f.readlines()):
    for i, c in enumerate(line.strip()):
      board[j][i] = int(c)

cell_to_neighbors = [set() for i in range(100)]

for j in range(10):
  for i in range(10):
    for t in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
      k, l = t
      if k >=0 and k < 10 and l >= 0 and l < 10:
        cell_to_neighbors[get_index(i, j)].add(get_index(k, l))

def substep(flashed):
  cont = False
  flashed_n_counts = [0 for i in range(100)]
  for j in range(10):
    for i in range(10):
      if board[j][i] > 9 and (get_index(i, j) not in flashed):
        flashed.add(get_index(i, j))
        for n in cell_to_neighbors[get_index(i, j)]:
          flashed_n_counts[n] += 1
  for j in range(10):
    for i in range(10):
      board[j][i] += flashed_n_counts[get_index(i, j)]
      if board[j][i] > 9 and (get_index(i, j) not in flashed):
        cont = True
  return cont

def step():
  flashed = set()
  for j in range(10):
    for i in range(10):
      board[j][i] += 1
  cont = False
  for j in range(10):
    for i in range(10):
      if board[j][i] > 9:
        cont = True
        break
    if cont:
      break
  while cont:
    cont = substep(flashed)
  for j in range(10):
    for i in range(10):
      if board[j][i] > 9:
        board[j][i] = 0

  return flashed

total = 0
for round in range(100):
  flashed = step()
  #print(flashed)
  total += len(flashed)

print(total)
