with open("advent_7.txt") as f:
  positions = [int(el) for el in f.readline().strip().split(",")]

positions.sort()

pos_sum = 0
for pos in positions:
  pos_sum += pos

x = int(pos_sum/len(positions))
current = 0
for pos in positions:
  if pos < x:
    current += (x-pos)*(x-pos+1)/2
  elif pos > x:
    current += (pos-x)*(pos-x+1)/2
print(current)
