import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N)]

for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  a -= 1
  b -= 1
  adj_list[b].append(a)

child_counts = [1 for _ in range(N)]

def flood_fill(node):
  visit = [False for _ in range(N)]
  que = deque()
  que.append(node)
  visit[node] = True
  cnt = 0
  while que:
    cur = que.popleft()
    cnt += 1
    nxts = adj_list[cur]
    for nxt in nxts:
      if visit[nxt]:
        continue
      visit[nxt] = True
      que.append(nxt)
  child_counts[node] = cnt

for i in range(N):
  flood_fill(i)

answer = []
maximum = max(child_counts)
for i in range(N):
  if child_counts[i] == maximum:
    answer.append(i + 1)

print(*answer)