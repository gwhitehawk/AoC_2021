from queue import LifoQueue

with open("advent_10.txt") as f:
  lines = [line.strip() for line in f.readlines()]

pairs = dict()
pairs["("] = ")"
pairs["{"] = "}"
pairs["["] = "]"
pairs["<"] = ">"

points = dict()
points[")"] = 1
points["]"] = 2
points["}"] = 3
points[">"] = 4

def process_line(line):
  q = LifoQueue(maxsize=0)
  q.put(line[0])
  for c in line[1:]:
    if c in pairs:
      q.put(c)
    else:
      top = q.get()
      if pairs[top] != c:
        return -1
  out = 0
  while not q.empty():
    top = q.get()
    out = 5*out + points[pairs[top]]
  return out

scores = []
for line in lines:
  line_score = process_line(line)
  if line_score > -1:
    scores.append(line_score)

scores.sort()

print(scores[int(len(scores)/2)])
