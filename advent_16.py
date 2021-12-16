import math

with open("advent_16.txt") as f:
  raw = f.readline().strip()

# raw = "C200B40A82"
bits = []
for c in raw:
  bin_str = bin(int(c, 16))[2:]
  l = len(bin_str)
  for _ in range(4 - l):
    bin_str = '0' + bin_str
  for b in bin_str:
    bits.append(int(b))


def parse_literal(start):
  current_index = start
  val = 0
  cont = True
  while cont:
    bit = bits[current_index]
    if bit == 0:
      cont = False
    for i in range(current_index + 1, current_index + 5):
      val = 2 * val + bits[i]
    current_index += 5
  return current_index, val


def apply_op(op, vals):
  if op == 0:
    return sum(vals)
  elif op == 1:
    return math.prod(vals)
  elif op == 2:
    return min(vals)
  elif op == 3:
    return max(vals)
  elif op == 5:
    return 1 if vals[0] > vals[1] else 0
  elif op == 6:
    return 1 if vals[0] < vals[1] else 0
  elif op == 7:
    return 1 if vals[0] == vals[1] else 0

  return vals[0]


def parse_packet(start):
  current_index = start
  v = 0
  for i in range(current_index, current_index + 3):
    v = 2 * v + bits[i]

  t = 0
  for i in range(current_index + 3, current_index + 6):
    t = 2 * t + bits[i]

  current_index += 6

  if t == 4:
    current_index, val = parse_literal(current_index)
  else:
    vals = []
    len_indicator = bits[current_index]
    sub_length = 0
    sub_count = 0

    if len_indicator == 0:
      for i in range(1, 16):
        sub_length = 2 * sub_length + bits[current_index + i]
      current_index += 16
    else:
      for i in range(1, 12):
        sub_count = 2 * sub_count + bits[current_index + i]
      current_index += 12

    packet_counter = 0
    length_counter = 0
    is_end = False
    while not is_end and current_index < len(bits):
      start = current_index
      current_index, current_val = parse_packet(start)
      vals.append(current_val)
      packet_counter += 1
      length_counter += current_index - start
      if length_counter == sub_length or packet_counter == sub_count:
        is_end = True
    val = apply_op(t, vals)

  return current_index, val

current_index, val = parse_packet(0)
print(val)
