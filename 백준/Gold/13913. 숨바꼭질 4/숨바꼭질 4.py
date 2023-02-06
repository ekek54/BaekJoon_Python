import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
dist = [0 for _ in range(100001)]
pre = [-1 for _ in range(100001)]
visit = [False for _ in range(100001)]

que = deque()
que.append(N)
visit[N] = True
while que:
  cur = que.popleft()
  nxts = [cur - 1, cur + 1, cur * 2]
  for nxt in nxts:
    if 0 <= nxt < 100001 and not visit[nxt]:
      dist[nxt] = dist[cur] + 1
      visit[nxt] = True
      pre[nxt] = cur
      que.append(nxt)
  if visit[K]:
    break
print(dist[K])
rev_root = [K]
while pre[K] != -1:
  rev_root.append(pre[K])
  K = pre[K]
print(*reversed(rev_root))
