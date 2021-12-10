with open("advent_3.txt") as f:
  lines = [line.strip() for line in f.readlines()]

lines.sort()
total = len(lines)

start = 0
end = total

for i in range(12):
  index = start
  zero_count = 0
  while lines[index][i] == "0":
    index += 1
    zero_count += 1
  if zero_count > (end-start)/2:
    end = index
  else:
    start = index
  if end-start < 2:
    break

oxy = lines[start]

start = 0
end = total

for i in range(12):
  index = start
  zero_count = 0
  while lines[index][i] == "0":
    index += 1
    zero_count += 1
  if zero_count <= (end-start)/2:
    end = index
  else:
    start = index
  if end-start < 2:
    break

co2 = lines[start]

o = 0
c = 0
for i in range(12):
  if oxy[i] == "1":
    o = 2*o + 1
  else:
    o *= 2
  if co2[i] == "1":
    c = 2*c + 1
  else:
    c *= 2

print(o*c)
