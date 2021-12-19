import copy
import math
import sys


with open("advent_18.txt") as f:
  lines = [line.strip() for line in f.readlines()]


class Node(object):
  def __init__(self, val, left=None, right=None, parent=None, is_left=True):
    self.val = val
    self.left = left
    self.right = right
    self.parent = parent
    self.is_left = is_left


def parse_line(line):
  if len(line) == 1:
    return Node(int(line))
  line = line[1:(len(line)-1)]
  right_start_index = 0
  left_counter = 0
  right_counter = 0
  for i, c in enumerate(line):
    if c == "[":
      left_counter += 1
    elif c == "]":
      right_counter += 1
    if left_counter == right_counter:
      right_start_index = i + 1
      break
  left = parse_line(line[:right_start_index])
  right = parse_line(line[right_start_index + 1:])
  current_node = Node(-1, left, right)
  left.parent = current_node
  left.is_left = True
  right.parent = current_node
  right.is_left = False
  return current_node


def get_rightmost_child(node):
  if node is None:
    return None
  while True:
    if node.val > -1:
      return node
    return get_rightmost_child(node.right)


def get_leftmost_child(node):
  if node is None:
    return None
  while True:
    if node.val > -1:
      return node
    return get_leftmost_child(node.left)


def get_rightmost_left_neighbor(node):
  if not node.is_left:
    return get_rightmost_child(node.parent.left)

  current = node
  while current is not None and current.parent is not None:
    if not current.is_left:
      return get_rightmost_child(current.parent.left)
    current = current.parent
  return None


def get_leftmost_right_neighbor(node):
  if node.is_left:
    if node.parent is not None:
      return get_leftmost_child(node.parent.right)
    return None
  current = node
  while current is not None and current.parent is not None:
    if current.is_left:
      return get_leftmost_child(current.parent.right)
    current = current.parent
  return None


def to_str(node):
  if node is None:
    return ""
  if node.val > -1:
    return node.val
  left_str = to_str(node.left)
  right_str = to_str(node.right)
  return "[{},{}]".format(left_str, right_str)


def split(node, should_split):
  if not should_split:
    return False
  if node.val >= 10:
    node.left = Node(math.floor(node.val/2))
    node.right = Node(math.ceil(node.val/2))
    node.val = -1
    node.left.parent = node
    node.left.is_left = True
    node.right.parent = node
    node.right.is_left = False
    return False
  elif node.val == -1:
    should_split = split(node.left, should_split)
    should_split = split(node.right, should_split)
  return should_split


def explode(node):
  if node is None or node.val > -1:
    return node

  is_shallow = node.parent is None or node.parent.parent is None or node.parent.parent.parent is None or node.parent.parent.parent.parent is None
  if is_shallow or node.left.val == -1 or node.right.val == -1:
    explode(node.left)
    explode(node.right)
    return node

  rightmost_left_neighbor_of_left = get_rightmost_left_neighbor(node.left)
  if rightmost_left_neighbor_of_left is not None:
    rightmost_left_neighbor_of_left.val += node.left.val
  leftmost_right_neighbor_of_right = get_leftmost_right_neighbor(node.right)
  if leftmost_right_neighbor_of_right is not None:
    leftmost_right_neighbor_of_right.val += node.right.val

  node.val = 0
  node.left = None
  node.right = None
  return node


def reduce(node):
  current_str = to_str(node)
  node = explode(node)
  exploded_str = to_str(node)
  while current_str != exploded_str:
    current_str = exploded_str
    node = explode(node)
    split(node, True)
    exploded_str = to_str(node)

  return node


def sum(node1, node2):
  top_node = Node(-1, node1, node2)
  node1.is_left = True
  node1.parent = top_node
  node2.is_left = False
  node2.parent = top_node
  return reduce(top_node)


orig_nodes = [parse_line(line) for line in lines]
nodes = copy.deepcopy(orig_nodes)

top = nodes[0]
for node in nodes[1:]:
  top = sum(top, node)
  # print(to_str(top))


def get_magnitude(node):
  if node.val > -1:
    return node.val
  else:
    return 3 * get_magnitude(node.left) + 2 * get_magnitude(node.right)


print(get_magnitude(top))
sys.exit(0)


max_m = 0
for i in range(len(nodes)):
  for j in range(len(nodes)):
    if i == j:
      continue
    inodes = copy.deepcopy(orig_nodes)
    m1 = get_magnitude(sum(inodes[i], inodes[j]))
    inodes = copy.deepcopy(orig_nodes)
    m2 = get_magnitude(sum(inodes[j], inodes[i]))
    max_m = max([m1, m2, max_m])
    # print("({}, {}): {}".format(i, j, max_m))

print(max_m)
