with open("advent_7.txt") as f:
  positions = [int(el) for el in f.readline().strip().split(",")]

positions.sort()

mid = int(len(positions)/2)

current = 0
for i in range(mid):
  current += positions[mid+i]-positions[i]

print(current)

