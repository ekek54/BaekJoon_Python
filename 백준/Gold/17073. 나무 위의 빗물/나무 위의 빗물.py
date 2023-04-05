import sys
from collections import deque

N, W = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N)]
in_degrees = [0 for _ in range(N)]
water = [0 for _ in range(N)]
water[0] = W
que = deque()
for _ in range(N - 1):
  u, v = map(int, sys.stdin.readline().split())
  u -= 1
  v -= 1
  adj_list[u].append(v)
  adj_list[v].append(u)
  in_degrees[u] += 1
  in_degrees[v] += 1

que.append(0)
visit = [False for _ in range(N)]
visit[0] = True
leaf_water = 0
leaf_cnt = 0
while que:
  cur = que.popleft()
  nxts = adj_list[cur]
  child_cnt = 0
  for nxt in nxts:
    if not visit[nxt]:
      child_cnt += 1

  if child_cnt == 0:
    leaf_cnt += 1
    leaf_water += water[cur]
    continue

  for nxt in nxts:
    if visit[nxt]: continue
    visit[nxt] = True
    que.append(nxt)
    water[nxt] = water[cur] / child_cnt

#print(water)
#print(leaf_cnt)
#print(leaf_water)
print(leaf_water / leaf_cnt)
