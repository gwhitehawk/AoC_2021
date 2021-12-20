with open("advent_19.txt") as f:
  lines = [line.strip() for line in f.readlines()]

reports = []

beacons = []

for line in lines:
  if line == "":
    reports.append(beacons)
  elif "scanner" in line:
    beacons = []
  else:
    coords = [int(c) for c in line.split(",")]
    beacons.append(coords)
reports.append(beacons)

def get_same_formation_pairs():
  distances = []
  for report in reports:
    distance_map = [[-1 for _ in range(len(report))] for _ in range(len(report))]
    for i in range(len(report)):
      for j in range(i+1, len(report)):
        d = (report[i][0]-report[j][0])**2 + (report[i][1]-report[j][1])**2 + (report[i][2]-report[j][2])**2
        distance_map[i][j] = d
        distance_map[j][i] = d
    distances.append(distance_map)

  same_formation_pairs = []
  vertex_map = [[dict() for _ in range(len(reports))] for _ in range(len(reports))]
  for i in range(len(reports)):
    for j in range(i+1, len(reports)):
      for k in range(len(distances[i])):
        for l in range(len(distances[j])):
          common_dist = len(set(distances[i][k]).intersection(set(distances[j][l])))
          if common_dist >= 12:
            vertex_map[i][j][k] = l
            vertex_map[j][i][l] = k
      j_cover = [p[0] for p in same_formation_pairs if p[1] == j]
      if len(vertex_map[i][j]) >= 12 and len(j_cover) == 0:
        print("Scanner {}: scanner {}".format(i, j))
        same_formation_pairs.append([i, j])

  return same_formation_pairs, vertex_map

def hash(vector):
  return "{},{},{}".format(vector[0], vector[1], vector[2])


def get_position(hash_str):
  return [int(c) for c in hash_str.split(",")]


permutations = [[[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[1, 0, 0], [0, 0, 1], [0, 1, 0]], [[0, 1, 0], [1, 0, 0], [0, 0, 1]], [[0, 1, 0], [0, 0, 1], [1, 0, 0]], [[0, 0, 1], [1, 0, 0], [0, 1, 0]], [[0, 0, 1], [0, 1, 0], [1, 0, 0]]]

orientations = []
for sign1 in [-1, 1]:
  for sign2 in [-1, 1]:
    for sign3 in [-1, 1]:
      for p in permutations:
        orientations.append([[sign1 * el for el in p[0]], [sign2 * el for el in p[1]], [sign3 * el for el in p[2]]])


def matrix_multi(matrix, vector):
  result = []
  for i in range(len(vector)):
    res = 0
    for j in range(len(vector)):
      res += matrix[i][j]*vector[j]
    result.append(res)
  return result


def vector_diff(v1, v2):
  result = []
  for i in range(len(v1)):
    result.append(v2[i]-v1[i])
  return result


def map_origin(points1, points2):
  possible_origins = set()
  orientation_to_coord = []
  for i, point in enumerate(points1):
    point2 = points2[i]
    origins = []
    for o in orientations:
      p2 = matrix_multi(o, point2)
      hash_str = hash(vector_diff(point, p2))
      origins.append(hash_str)
      if i == 0:
        orientation_to_coord.append(hash_str)

    if len(possible_origins) == 0:
      possible_origins = set(origins)
    else:
      possible_origins = possible_origins.intersection(set(origins))
    if len(possible_origins) == 1:
      break
  origin_str = [el for el in possible_origins][0]
  origin = get_position(origin_str)
  for i, o in enumerate(orientations):
    if orientation_to_coord[i] == origin_str:
      return o, [-c for c in origin]


origin_from_0 = [[0, 0, 0]]
def transform(same_formation_pairs, vertex_map):
  for pair in same_formation_pairs:
    point_map = vertex_map[pair[0]][pair[1]]
    points1 = []
    points2 = []
    for k, v in point_map.items():
      points1.append(reports[pair[0]][k])
      points2.append(reports[pair[1]][v])
    print("Origin of scanner {} relative to scanner {}:".format(pair[1], pair[0]))
    orientation, origin = map_origin(points1, points2)
    #print(orientation)
    print(origin)
    if pair[0] == 0:
      origin_from_0.append(origin)
    for i in range(len(reports[pair[1]])):
      point = reports[pair[1]][i]
      point_in_rf = [-c for c in vector_diff(matrix_multi(orientation, point), [-c for c in origin])]
      if i not in vertex_map[pair[0]][pair[1]].values():
        reports[pair[0]].append(point_in_rf)


same_formation_pairs, vertex_map = get_same_formation_pairs()
transform(same_formation_pairs, vertex_map)
transformed = False

while not transformed:
  same_formation_pairs, vertex_map = get_same_formation_pairs()
  connected_to_0 = []
  for pair in same_formation_pairs:
    if pair[0] == 0:
      connected_to_0.append(pair[1])
  transformed = len(connected_to_0) == len(reports) - 1
  transform(same_formation_pairs, vertex_map)

h = len(set([hash(p) for p in reports[0]]))
print(h)

max_d = 0
for i in range(len(origin_from_0)):
  for j in range(i+1, len(origin_from_0)):
    first = origin_from_0[i]
    second = origin_from_0[j]
    max_d = max(abs(first[0]-second[0])+abs(first[1]-second[1])+abs(first[2]-second[2]), max_d)

print(max_d)
