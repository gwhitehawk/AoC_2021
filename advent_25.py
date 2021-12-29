import copy

with open("advent_25.txt") as f:
  lines = [line.strip() for line in f.readlines()]

h = len(lines)
w = len(lines[0])

class Cell(object):
  def __init__(self, state):
    self.state = state

  def empty(self):
    return self.state == 0

  def __eq__(self, other):
    return isinstance(other, Cell) and self.state == other.state

board = [[Cell(0) for _ in range(w)] for _ in range(h)]

for j, line in enumerate(lines):
  for i, c in enumerate(line):
    if c == ">":
      board[j][i] = Cell(1)
    elif c == "v":
      board[j][i] = Cell(2)

def move(board):
  moves = 0
  new_board = copy.deepcopy(board)
  for j in range(h):
    for i in range(w):
      if board[j][i].state == 1 and board[j][(i+1)%w].state == 0:
        new_board[j][(i+1)%w].state = 1
        new_board[j][i].state = 0
        moves += 1
  board = new_board
  new_board = copy.deepcopy(board)
  for j in range(h):
    for i in range(w):
      if board[j][i].state == 2 and board[(j+1)%h][i].state == 0:
        new_board[(j+1)%h][i].state = 2
        new_board[j][i].state = 0
        moves += 1
  return new_board, moves

board, moves = move(board)
counter = 1
while moves > 0:
  board, moves = move(board)
  print(moves)
  counter += 1

print(counter)
