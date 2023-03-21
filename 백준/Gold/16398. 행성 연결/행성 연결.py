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


N = int(sys.stdin.readline())
parent = [i for i in range(N)]
flow_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0
flows = []

for i in range(N - 1):
  for j in range(i + 1, N):
    flow = (i, j, flow_board[i][j])
    flows.append(flow)

flows.sort(key=lambda x: x[2])

for flow in flows:
  i, j, cost = flow
  if union(i, j, parent):
    answer += cost

print(answer)
