import math

target_x_range = [217, 240]
target_y_range = [-126, -69]

# sqrt(2*min(target_x_range)), because max x distance traveled is x(x+1)/2
min_x = math.ceil(math.sqrt(target_x_range[0]*2))
max_x = target_x_range[1]

# if target reached with 1 step
min_y = target_y_range[0]
# total 2*|target_y_range[0]| steps, last from 0 to target_y_range[0]
max_y = -target_y_range[0] - 1

speeds = 0
for x in range(min_x, max_x + 1):
  for y in range(max_y, min_y - 1, -1):
    current_x = 0
    current_y = 0
    speed_x = x
    speed_y = y
    hit = False
    while current_x < target_x_range[0] or current_y > target_y_range[1]:
      current_x += speed_x
      current_y += speed_y
      if current_x in range(target_x_range[0], target_x_range[1] + 1) and current_y in range(target_y_range[0], target_y_range[1] + 1):
        hit = True
      if speed_x > 0:
        speed_x -= 1
      speed_y -= 1
    if hit:
      speeds += 1

print(speeds)
