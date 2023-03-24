import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
que = deque()
cnt = 0
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def next_to_cheeze(rc):
  r, c = rc
  for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    if 0 <= nr < N and 0 <= nc < M:
      if board[nr][nc] == 1:
        return True
  return False


def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')


while True:
  melt_cheeze = []
  #pb(board)
  visit = [[0 for j in range(M)] for i in range(N)]
  remove_cheeze = 0
  flag = False
  que.append((0, 0))
  visit[0][0] = 1
  while que:
    cur_r, cur_c = que.popleft()
    for i in range(4):
      nr = cur_r + dr[i]
      nc = cur_c + dc[i]
      if 0 <= nr < N and 0 <= nc < M:
        if visit[nr][nc] and board[nr][nc] == 0:
          continue
        if board[nr][nc] == 0:
          visit[nr][nc] = 1
          que.append((nr, nc))
        else:
          visit[nr][nc] += 1
          if visit[nr][nc] == 2:
            melt_cheeze.append((nr, nc))

  if not melt_cheeze:
    break
  for melt_c in melt_cheeze:
    r, c = melt_c
    board[r][c] = 0
  cnt += 1
print(cnt)
