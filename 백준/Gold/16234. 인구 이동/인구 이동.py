import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


def migration():
  que = deque()
  visit = [[False for j in range(N)] for i in range(N)]
  res = False
  for i in range(N):
    for j in range(N):
      if visit[i][j]:
        continue
      que.append([i, j])
      visit[i][j] = True
      union = bfs(que, visit)
      if len(union) > 1:
        res = True
        sum_of_union = sum([A[union[k][0]][union[k][1]] for k in range(len(union))])
        for k in range(len(union)):
          A[union[k][0]][union[k][1]] = sum_of_union // len(union)
  return res

def oob(r, c):
  return not (0 <= r < N and 0 <= c < N)


def bfs(que: deque, visit):
  dr = [1, -1, 0, 0]
  dc = [0, 0, 1, -1]
  union = []
  while que:
    cur_r, cur_c = que.popleft()
    union.append([cur_r, cur_c])
    for i in range(4):
      nr = cur_r + dr[i]
      nc = cur_c + dc[i]
      if oob(nr, nc):
        continue
      if visit[nr][nc]:
        continue
      if L <= abs(A[nr][nc] - A[cur_r][cur_c]) <= R:
        que.append([nr, nc])
        visit[nr][nc] = True
  return union


cnt = 0
while migration():
  cnt += 1
print(cnt)