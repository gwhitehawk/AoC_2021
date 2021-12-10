with open("advent_2.txt") as f:
  lines = f.readlines()

x = 0
y = 0
aim = 0

for line in lines:
  codeword, dist = line.strip().split()
  distance = int(dist)
  if codeword == "forward":
    x += distance
    y += distance * aim
  elif codeword == "up":
    aim -= distance
  else:
    aim += distance

print(x*y)
