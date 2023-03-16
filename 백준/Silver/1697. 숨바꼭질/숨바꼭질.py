import sys
from collections import deque

que = deque()

N, K = map(int, sys.stdin.readline().split())
que.append((N, 0))
visit = [False for _ in range(100001)]
while que:
  cur, dist = que.popleft()
  if cur == K:
    print(dist)
    break
  nxts = [cur + 1, cur - 1, cur * 2]
  for nxt in nxts:
    if nxt > 100000 or 0 > nxt:
      continue
    if visit[nxt]:
      continue
    visit[nxt] = True
    que.append((nxt, dist + 1))

