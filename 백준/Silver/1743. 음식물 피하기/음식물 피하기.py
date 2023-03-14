import sys
from collections import deque

answer = 0
N, M, K = map(int, sys.stdin.readline().split())
board = [[0 for j in range(M)] for i in range(N)]
for _ in range(K):
  r, c = map(int, sys.stdin.readline().split())
  r -= 1
  c -= 1
  board[r][c] = 1

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
visit = [[False for j in range(M)] for i in range(N)]
que = deque()
for i in range(N):
  for j in range(M):
    if visit[i][j]: continue
    if not board[i][j]: continue
    que.append((i, j))
    visit[i][j] = True
    size = 0
    while que:
      size += 1
      cur_r, cur_c = que.popleft()
      for k in range(4):
        nr = cur_r + dr[k]
        nc = cur_c + dc[k]
        if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc] and board[nr][nc]:
          que.append((nr, nc))
          visit[nr][nc] = True
    answer = max(answer, size)
print(answer)
