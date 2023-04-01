import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
indegree = [0 for _ in range(N)]
adj_list = [[] for _ in range(N)]
for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  a -= 1
  b -= 1
  adj_list[a].append(b)
  indegree[b] += 1

que = deque()
for i in range(N):
  if indegree[i] == 0:
    que.append(i)

ord = []
while que:
  cur = que.popleft()
  ord.append(cur + 1)
  nxts = adj_list[cur]
  for nxt in nxts:
    indegree[nxt] -= 1
    if indegree[nxt] == 0:
      que.append(nxt)

print(*ord)