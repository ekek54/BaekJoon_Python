import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
edge_list = deque()
parent = [i for i in range(N)]

def find(a):
  if a == parent[a]:
    return a
  else:
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
  a = find(a)
  b = find(b)
  if a < b:
    parent[b] = a
    return True
  elif a > b:
    parent[a] = b
    return True
  else:
    return False


for i in range(M):
  x, y = map(int, sys.stdin.readline().split())
  x -= 1
  y -= 1
  edge_list.append((x, y, i + 1))

answer = []
round = 0
while round < K:
  round += 1
  score = 0
  parent = [i for i in range(N)]
  cnt = 0
  #(edge_list)
  for i in range(len(edge_list)):
    x, y, w = edge_list[i]
    if union(x, y):
      score += w
      cnt += 1
    if cnt == N - 1:
      break

  if cnt == N - 1:
    edge_list.popleft()
    answer.append(score)
  else:
    break


while len(answer) != K:
  answer.append(0)

print(*answer)
