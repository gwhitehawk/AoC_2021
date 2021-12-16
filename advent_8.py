import queue
import copy

test_inputs = []
real_inputs = []

with open("advent_8.txt") as f:
  lines = [line.strip() for line in f.readlines()]

for line in lines:
  test, real = line.split("|")
  test_inputs.append(test.strip().split())
  real_inputs.append(real.strip().split())

dig_to_wires = []
dig_to_wires.append(set(["a", "b", "c", "e", "f", "g"]))
dig_to_wires.append(set(["c", "f"]))
dig_to_wires.append(set(["a", "c", "d", "e", "g"]))
dig_to_wires.append(set(["a", "c", "d", "f", "g"]))
dig_to_wires.append(set(["b", "c", "d", "f"]))
dig_to_wires.append(set(["a", "b", "d", "f", "g"]))
dig_to_wires.append(set(["a", "b", "d", "e", "f", "g"]))
dig_to_wires.append(set(["a", "c", "f"]))
dig_to_wires.append(set(["a", "b", "c", "d", "e", "f", "g"]))
dig_to_wires.append(set(["a", "b", "c", "d", "f", "g"]))

def init_map(garbled, current_map):
  intersects = dict()
  for sym in dig_to_wires[8]:
    intersects[sym] = []

  for dig in range(10):
    if len(dig_to_wires[dig]) == len(garbled):
      # if garbled digit length matches digit repr. length, map each segment
      # to real segment possibilities (included segment to repr. segments,
      # missing segment to complement of repr. segment set.
      for sym in dig_to_wires[8]:
        if sym in garbled:
          to_update = dig_to_wires[dig]
        else:
          to_update = dig_to_wires[8].difference(dig_to_wires[dig])
        # if segment already has a restricted possible image set,
        # only record intersection. E.g. if "a" newly appears to be in
        # two-segment set, it must map to image of "1", previous larger
        # image set is therefore restricted.
        if sym in current_map:
          intersects[sym].append(to_update.intersection(current_map[sym]))
        else:
          intersects[sym].append(to_update)

  # We made assumption on garbled being any of the digits represented
  # by the same number of segments. For each, we got possible mappings
  # of each segment. We don't know which digit garbled maps to, take
  # the union.
  for sym in garbled:
    current_map[sym] = set()
    for el in intersects[sym]:
      current_map[sym] = current_map[sym].union(el)

# Try map all 7 segments. There are multiple possibilities for some
# segments, consider all allowed mappings.
def decode(real_inputs, current_map):
  q = queue.Queue(maxsize=0)
  q.put(dict())
  dicts = []
  while not q.empty():
    temp_map = q.get()
    if len(temp_map.keys()) == 7:
      dicts.append(temp_map)
    for key in current_map:
      if key not in temp_map:
        for image in current_map[key]:
          if image not in temp_map.values():
            new_map = copy.deepcopy(temp_map)
            new_map[key] = image
            q.put(new_map)
        break

  # For each possibility, check that the assumed
  # segment map defines valid 4 digits. When valid
  # mapping is found, output it.
  for d in dicts:
    output = []
    for garbled in real_inputs:
      im = set()
      for sym in garbled:
        im.add(d[sym])
      for dig in range(10):
        if dig_to_wires[dig] == im:
          output.append(dig)
          break
    if len(output) == 4:
      return output
  return []

def update_map(current_map):
  counter = 2
  while max([len(current_map[x]) for x in current_map]) > 1 and counter > 0:
    # If union of images has the same size as union of preimages, there
    # must be a bijection between the two sets in the resulting
    # segment map. Given that there's a bijection, we can remove the segments
    # in the image from the possible image sets corresponding to other segments
    # than the considered preimages.
    for first in current_map:
      for second in current_map:
        un = current_map[first].union(current_map[second])
        if len(un) == len(set([first, second])):
          for other in current_map:
            if other not in set([first, second]):
              current_map[other] = current_map[other].difference(un)
    counter -= 1

total = 0
for i in range(len(test_inputs)):
  current_map = dict()
  all_ins = test_inputs[i] + real_inputs[i]
  for garbled in all_ins:
    init_map(garbled, current_map)
  update_map(current_map)
  out = decode(real_inputs[i], current_map)
  total = total + 1000*out[0] + 100*out[1] + 10*out[2] + out[3]
  #print(out)

print(total)


