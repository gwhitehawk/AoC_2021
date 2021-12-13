class Instruction(object):
  def __init__(self, coord, is_x):
    self.coord = coord
    self.is_x = is_x


class Point(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def fold(self, instruction):
    if instruction.is_x and self.x > instruction.coord:
      self.x = 2 * instruction.coord - self.x
    elif not instruction.is_x and self.y > instruction.coord:
      self. y = 2 * instruction.coord - self.y

  def get_index(self):
    return 1000 * self.y + self.x


with open("advent_13.txt") as f:
  lines = [line.strip() for line in f.readlines()]

points = set()
instructions = []

read_points = True
for line in lines:
  if line == "":
    read_points = False
    continue
  if read_points:
    x, y = line.split(",")
    points.add(Point(int(x), int(y)))
  else:
    coord = int(line.split("=")[1])
    instructions.append(Instruction(coord, "x=" in line))

folded = set()

for instruction in instructions:
  for point in points:
    point.fold(instruction)

for point in points:
  folded.add(point.get_index())

min_x = min([index % 1000 for index in folded])
max_x = max([index % 1000 for index in folded])
min_y = min([int(index / 1000) for index in folded])
max_y = max([int(index / 1000) for index in folded])

for y in range(0, max_y - min_y + 1):
  x_line = []
  for x in range(0, max_x - min_x +  1):
    if (1000*(y+min_y) + (x+min_x)) in folded:
      x_line.append("#")
    else:
      x_line.append(".")
  print("".join(x_line))

