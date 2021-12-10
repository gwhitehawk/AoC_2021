with open("advent_1.txt") as f:
  lines = [int(line.strip()) for line in f.readlines()]

inc = 0
first = lines[0]
second = lines[1]
third = lines[2]
prev = lines[0] + lines[1] + lines[2]
for line in lines[3:]:
  current = prev + line - first
  if prev < current:
    inc += 1
  first = second
  second = third
  third = line
  prev = current

print(inc)
