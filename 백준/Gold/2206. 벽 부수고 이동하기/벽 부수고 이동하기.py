import sys
from collections import deque
from math import inf

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
src = (0, 0)
des = (N - 1, M - 1)

def calc_dist_from(rc):
  r, c = rc
  dist = [[inf for j in range(M)] for i in range(N)]
  dr = [1, -1, 0, 0]
  dc = [0, 0, 1, -1]
  que = deque()
  que.append(rc)
  dist[r][c] = 1
  while que:
    cur_r, cur_c = que.popleft()
    cur_dist = dist[cur_r][cur_c]
    for i in range(4):
      nr = cur_r + dr[i]
      nc = cur_c + dc[i]
      if 0 <= nr < N and 0 <= nc < M:
        if dist[nr][nc] != inf: continue
        dist[nr][nc] = cur_dist + 1
        if board[nr][nc] == 0:
          que.append((nr, nc))
  return dist


def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')

def is_breakable(r, c):
  dr = [1, -1, 0, 0]
  dc = [0, 0, 1, -1]
  if board[r][c] != 1:
    return False
  else:
    cnt = 0
    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if 0 <= nr < N and 0 <= nc < M:
        if board[nr][nc] == 0:
          cnt += 1
    return True if cnt >= 2 else False

dist_from_src = calc_dist_from(src)
dist_from_des = calc_dist_from(des)
answer = dist_from_src[N - 1][M - 1]
for i in range(N):
  for j in range(M):
    if is_breakable(i, j):
      answer = min(answer, dist_from_src[i][j] + dist_from_des[i][j] - 1)

print(answer if answer != inf else -1)