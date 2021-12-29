with open("advent_22.txt") as f:
  lines = [line.strip() for line in f.readlines()]

class Instruction(object):
  def __init__(self, instruction, ranges):
    self.instruction = instruction
    self.ranges = ranges

def center_intersection(ranges):
  intersection = []
  for i in range(3):
    if ranges[i][0]<=50 and ranges[i][1]>=-50:
      intersection.append([max(ranges[i][0], -50), min(ranges[i][1], 50)])
  return intersection

instructions = []
valid = 0
for line in lines:
  instr, coords = line.split()
  instruction = 0
  if instr == "on":
    instruction = 1
  xyz = [c.split("=")[1] for c in coords.split(",")]
  ranges = []
  for i in range(3):
    ranges.append([int(el) for el in xyz[i].split("..")])
  restriction = center_intersection(ranges)
  if len(restriction) == 3:
    valid += 1
    instructions.append(Instruction(instruction, center_intersection(ranges)))

print("valid intervals: {}".format(valid))

states = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
for instruction in instructions:
  for i in range(3):
    for j in range(instruction.ranges[2][0]+50, instruction.ranges[2][1]+51):
      for k in range(instruction.ranges[1][0]+50, instruction.ranges[1][1]+51):
        for l in range(instruction.ranges[0][0]+50, instruction.ranges[0][1]+51):
          states[l][k][j] = instruction.instruction

counter = 0
for j in range(101):
  for k in range(101):
    for l in range(101):
      if states[l][k][j] == 1:
        counter += 1
print(counter)
