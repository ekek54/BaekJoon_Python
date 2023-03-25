import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())


def find(a, parent):
  if parent[a] == a:
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


# cycle 여부 판단
def is_acycle(adj_list):
  N = len(adj_list)
  parent = [i for i in range(N)]

  for i in range(N):
    for j in range(len(adj_list[i])):
      if not union(i, adj_list[i][j], parent):
        return False
  return True


in_degree = [0 for _ in range(N)]
adj_list = [[] for _ in range(N)]
visit = [False for _ in range(N)]
que = deque()
answer = []

for _ in range(M):
  order = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))[1:]
  for i in range(len(order) - 1):
    a, b = order[i], order[i + 1]
    adj_list[a].append(b)
    in_degree[b] += 1

for i in range(len(in_degree)):
  if in_degree[i] == 0:
    que.append(i)
    visit[i] = True

while que:
  cur = que.popleft()
  answer.append(cur)
  for i in range(len(adj_list[cur])):
    nxt = adj_list[cur][i]
    if visit[nxt]:
      continue
    in_degree[nxt] -= 1
    if in_degree[nxt] == 0:
      visit[nxt] = True
      que.append(nxt)
if sum(in_degree) != 0:
  print(0)
else:
  for a in answer:
    print(a + 1)