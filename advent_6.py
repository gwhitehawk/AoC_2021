with open("advent_6.txt") as f:
  fishes = [int(el) for el in f.readline().strip().split(",")]

counter_counts = [0 for i in range(9)]
for fish in fishes:
  counter_counts[fish] += 1

print(counter_counts)

for i in range(256):
  mom_count = counter_counts[0]
  for i in range(1, 9):
    counter_counts[i-1] = counter_counts[i]
  counter_counts[6] += mom_count
  counter_counts[8] = mom_count
  print(counter_counts)

total = 0
for i in range(9):
  total += counter_counts[i]

print(total)
