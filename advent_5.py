with open("advent_5.txt") as f:
  lines = [line.strip() for line in f.readlines()]


class Point(object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __eq__(self, obj):
    return isinstance(obj, Point) and self.x == obj.x and self.y == obj.y


class Pipe(object):
  def __init__(self, start, end):
    self.start = start
    self.end = end


pipes = []


for line in lines:
  start, end = line.split("->")
  start_coords = [int(el.strip()) for el in start.strip().split(",")]
  start_point = Point(start_coords[0], start_coords[1])
  end_coords = [int(el.strip()) for el in end.strip().split(",")]
  end_point = Point(end_coords[0], end_coords[1])

  if start_point.x == end_point.x:
    if start_point.y < end_point.y:
      pipes.append(Pipe(start_point, end_point))
    else:
      pipes.append(Pipe(end_point, start_point))
  elif start_point.y == end_point.y:
    if start_point.x < end_point.x:
      pipes.append(Pipe(start_point, end_point))
    else:
      pipes.append(Pipe(end_point, start_point))
  else:
    if start_point.x < end_point.x:
      pipes.append(Pipe(start_point, end_point))
    else:
      pipes.append(Pipe(end_point, start_point))


cross_count = dict()

for pipe in pipes:
  if pipe.start.x == pipe.end.x:
    for i in range(pipe.start.y, pipe.end.y + 1):
      p = 1000*pipe.start.x + i
      if p not in cross_count:
        cross_count[p] = 1
      else:
        cross_count[p] += 1
  elif pipe.start.y == pipe.end.y:
    for i in range(pipe.start.x, pipe.end.x + 1):
      p = 1000*i + pipe.start.y
      if p not in cross_count:
        cross_count[p] = 1
      else:
        cross_count[p] += 1
  else:
    if pipe.start.y < pipe.end.y:
      for i in range(pipe.start.x, pipe.end.x + 1):
        p = 1000*i + pipe.start.y + (i - pipe.start.x)
        if p not in cross_count:
          cross_count[p] = 1
        else:
          cross_count[p] += 1
    else:
      for i in range(pipe.start.x, pipe.end.x + 1):
        p = 1000*i + pipe.start.y - (i - pipe.start.x)
        if p not in cross_count:
          cross_count[p] = 1
        else:
          cross_count[p] += 1

crossroads = 0
for k in cross_count:
  if cross_count[k] > 1:
    crossroads += 1

print(crossroads)
