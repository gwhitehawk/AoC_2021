from queue import LifoQueue

with open("advent_10.txt") as f:
  lines = [line.strip() for line in f.readlines()]

pairs = dict()
pairs["("] = ")"
pairs["{"] = "}"
pairs["["] = "]"
pairs["<"] = ">"

points = dict()
points[")"] = 3
points["]"] = 57
points["}"] = 1197
points[">"] = 25137

def process_line(line):
  q = LifoQueue(maxsize=0)
  q.put(line[0])
  for c in line[1:]:
    if c in pairs:
      q.put(c)
    else:
      top = q.get()
      if c != pairs[top]:
        return points[c]
  return 0

total = 0
for line in lines:
  total += process_line(line)

print(total)
