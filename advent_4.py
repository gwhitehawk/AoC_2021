with open("advent_4.txt") as f:
  lines = [line.strip() for line in f.readlines()]

draws = [int(draw) for draw in lines[0].split(",")]
boards = []

current_board = [[-1 for j in range(5)] for i in range(5)]
current_row = 0

for index, val in enumerate(lines):
  if index < 2:
    continue
  if (index - 2) % 6 < 5:
    row = [int(num) for num in val.split()]
    for j, number in enumerate(row):
      current_board[current_row][j] = number
    current_row += 1
  else:
    boards.append(current_board)
    current_board = [[-1 for j in range(5)] for j in range(5)]
    current_row = 0

class CoordMark(object):
  def __init__(self, i, j, marked):
    self.i = i
    self.j = j
    self.marked = marked

board_maps = []
for board in boards:
  num_to_coord = dict()
  for i in range(5):
    for j in range(5):
      num_to_coord[board[i][j]] = CoordMark(i, j, False)
  board_maps.append(num_to_coord)

row_counters = []
col_counters = []
for board in boards:
  row_counters.append([0 for i in range(5)])
  col_counters.append([0 for i in range(5)])

won = False
win_ind = -1
win_draw = -1

for draw in draws:
  for ind, board_map in enumerate(board_maps):
    if draw in board_map:
      board_map[draw].marked = True
      row_counters[ind][board_map[draw].i] += 1
      col_counters[ind][board_map[draw].j] += 1
      if row_counters[ind][board_map[draw].i] == 5 or col_counters[ind][board_map[draw].j] == 5:
        won = True
        win_ind = ind
        win_draw = draw
        print("draw: {}, board: {}".format(draw, ind))
        #print(boards[ind][board_map[draw].i])
        #print([boards[ind][i][board_map[draw].j] for i in range(5)])
        break
  if won:
    break

unmarked_sum = 0
for k in board_maps[win_ind]:
  if not board_maps[win_ind][k].marked:
    unmarked_sum += k

print(boards[win_ind])
print(unmarked_sum*win_draw)
