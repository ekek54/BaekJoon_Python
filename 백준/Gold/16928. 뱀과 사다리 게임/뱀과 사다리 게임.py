import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
ladder = [i for i in range(100)]
snake = [i for i in range(100)]
dist = [-1 for _ in range(100)]

for _ in range(N):
  x, y = map(int, sys.stdin.readline().split())
  x -= 1
  y -= 1
  ladder[x] = y

for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())
  u -= 1
  v -= 1
  snake[u] = v

que = deque()
que.append(0)
dist[0] = 0
while que:
  cur = que.popleft()
  if cur == 99:
    break
  for i in range(6):
    nxt = cur + (i + 1)
    if nxt >= 100: continue
    if ladder[nxt] != nxt:
      nxt = ladder[nxt]
    elif snake[nxt] != nxt:
      nxt = snake[nxt]
    if dist[nxt] != -1: continue
    dist[nxt] = dist[cur] + 1
    que.append(nxt)

print(dist[99])
