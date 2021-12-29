import sys

with open("advent_21.txt") as f:
  positions = [int(x.strip().split(":")[1]) for x in f.readlines()]


def mod_10(i):
  return i % 10 if i % 10 > 0 else 10


scores = [0, 0]


def score_move(k, current, player):
  return mod_10(current + 18 * k + 6 + 9 * player)


k = 0
while max(scores) < 1000:
  positions[0] = score_move(k, positions[0], 0)
  scores[0] += positions[0]
  if scores[0] > 1000:
    print("{}: {}".format(k, scores))
    print(scores[1] * (6 * (k+1) + 3))
    sys.exit(0)
  positions[1] = score_move(k, positions[1], 1)
  scores[1] += positions[1]
  k += 1

print("{}: {}".format(k, scores))
print(6 * k * scores[0])
