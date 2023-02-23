import sys
from collections import deque

def append_adj(adj_dict, a, b):
  if a in adj_dict:
    adj_dict[a].append(b)
  else:
    adj_dict[a] = [b]


def make_adj_dict(arr):
  result = {}
  parent_idx = -1
  for i in range(1, n):
    if arr[i] != arr[i - 1] + 1:
      parent_idx += 1
    parent = arr[parent_idx]
    child = arr[i]
    append_adj(result, parent, child)
  return result

def my_parent(tree: dict, me):
  for parent, childs in tree.items():
    if me in childs:
      return parent

def my_grandparent(tree, me):
  return my_parent(tree, my_parent(tree, me))

def search_cousin(tree, root, me):
  que = deque()
  que.append((0, 0, root))
  grandparent = my_grandparent(tree, me)
  parent = my_parent(tree, me)
  cnt = 0
  while que:
    cur_grandparent, cur_parent, cur = que.popleft()
    if cur_grandparent == grandparent and cur_parent != parent:
      cnt += 1
    if cur in tree:
      for child in tree[cur]:
        nxt = (cur_parent, cur, child)
        que.append(nxt)
  return cnt

while True:
  n, k = map(int, sys.stdin.readline().split())
  if (n, k) == (0, 0):
    break
  arr = list(map(int, sys.stdin.readline().split()))
  root = arr[0]
  adj_dict = make_adj_dict(arr)
  print(search_cousin(adj_dict, root, k))

