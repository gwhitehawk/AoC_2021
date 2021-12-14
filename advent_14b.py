sub = dict()

with open("advent_14.txt") as f:
  poly_input = f.readline().strip()
  f.readline()
  for line in f.readlines():
    source, insert = line.strip().split("->")
    sub[source.strip()] = insert.strip()

bigram_counts = dict.fromkeys(sub.keys(), 0)

for i in range(len(poly_input)-1):
  bigram_counts[poly_input[i]+poly_input[i+1]] += 1

for i in range(40):
  diff_counts = dict.fromkeys(sub.keys(), 0)
  for bigram in sub.keys():
    if bigram_counts[bigram] == 0:
      continue
    c = sub[bigram]
    new_1 = bigram[0] + c
    new_2 = c + bigram[1]
    diff_counts[new_1] += bigram_counts[bigram]
    diff_counts[new_2] += bigram_counts[bigram]
    diff_counts[bigram] += -bigram_counts[bigram]
  for bigram in diff_counts:
    bigram_counts[bigram] += diff_counts[bigram]

first_char = poly_input[0]
last_char = poly_input[len(poly_input)-1]

char_counts = dict()
for key in bigram_counts:
  for c in key:
    if c not in char_counts:
      char_counts[c] = bigram_counts[key]
    else:
      char_counts[c] += bigram_counts[key]

for key in char_counts:
  if key == first_char or key == last_char:
    char_counts[key] = (char_counts[key] + 1)/2
  else:
    char_counts[key] = char_counts[key]/2

max_o = max(char_counts.values())
min_o = min(char_counts.values())
print(max_o - min_o)
