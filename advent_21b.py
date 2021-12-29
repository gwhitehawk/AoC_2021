import copy
from queue import LifoQueue

with open("advent_21.txt") as f:
  positions = [int(x.strip().split(":")[1]) for x in f.readlines()]

stack_counter = 0

def mod_10(i):
  return i % 10 if i % 10 > 0 else 10

goal = 21

triples = [0 for _ in range(7)]

for i in range(1, 4):
  for j in range(1, 4):
    for k in range(1, 4):
      triples[i+j+k-3] += 1

win_counts = [0, 0]

q = LifoQueue(maxsize = 0)

class State(object):
  def __init__(self, positions, scores, multiplicity):
    self.positions = positions
    self.scores = scores
    self.multiplicity = multiplicity

q.put(State(positions, [0, 0], 1))

while not q.empty():
  stack_counter += 1
  curr_state = q.get()
  print("stack counter: {}".format(stack_counter))
  print("stack get: {}".format(curr_state.scores))
  for i, t in enumerate(triples):
    s = copy.deepcopy(curr_state.scores)
    p = copy.deepcopy(curr_state.positions)
    p[0] = mod_10(p[0] + i + 3)
    s[0] += p[0]
    if s[0] >= goal:
      win_counts[0] += t * curr_state.multiplicity
    else:
      for j, u in enumerate(triples):
        s2 = copy.deepcopy(s)
        p2 = copy.deepcopy(p)
        p2[1] = mod_10(p2[1] + j + 3)
        s2[1] += p2[1]
        if s2[1] < goal:
          print("Stack put: {}".format(s2))
          q.put(State(p2, s2, curr_state.multiplicity * t * u))
        else:
          win_counts[1] += t * u * curr_state.multiplicity

print(win_counts)
