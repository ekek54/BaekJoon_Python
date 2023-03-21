import sys
from collections import deque


def find(a, parent):
  if a == parent[a]:
    return a
  else:
    parent[a] = find(parent[a], parent)
    return parent[a]


def union(a, b, parent):
  a = find(a, parent)
  b = find(b, parent)
  if a < b:
    parent[b] = a
    return True
  elif a > b:
    parent[a] = b
    return True
  else:
    return False


N, M = map(int, sys.stdin.readline().split())
entrance, first, c = map(int, sys.stdin.readline().split())
if c == 0:
  c = 1
else:
  c = 0
roads = []
for _ in range(M):
  A, B, C = map(int, sys.stdin.readline().split())
  if C == 0:
    C = 1
  else:
    C = 0
  roads.append(tuple([A, B, C]))
best_roads = sorted(roads, key=lambda x: x[2])
worst_roads = sorted(roads, key=lambda x: -x[2])

best_parent = [i for i in range(N + 1)]
worst_parent = [i for i in range(N + 1)]

best_cnt = c
union(entrance, first, best_parent)
for best_road in best_roads:
  A, B, C = best_road
  if union(A, B, best_parent):
    best_cnt += C

worst_cnt = c
union(entrance, first, worst_parent)
for worst_road in worst_roads:
  A, B, C = worst_road
  if union(A, B, worst_parent):
    worst_cnt += C
print(worst_cnt ** 2 - best_cnt ** 2)
