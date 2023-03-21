from collections import deque


def solution(board):
  N = len(board)
  M = len(board[0])
  answer = 0
  que = deque()
  visit = [[False for j in range(M)] for i in range(N)]
  for i in range(N):
    for j in range(M):
      if board[i][j] == 'G':
        goal = (i, j)
      if board[i][j] == 'R':
        visit[i][j] = True
        que.append((i, j, 0))

  dr = [1, -1, 0, 0]
  dc = [0, 0, 1, -1]
  while que:
    cur_r, cur_c, dist = que.popleft()
    if (cur_r, cur_c) == goal:
      return dist
    for i in range(4):
      d = 1
      while True:
        nr = cur_r + dr[i] * d
        nc = cur_c + dc[i] * d
        if 0 <= nr < N and 0 <= nc < M:
          if board[nr][nc] in ('.', 'R', 'G'):
            d += 1
          elif board[nr][nc] == 'D':
            nr = cur_r + dr[i] * (d - 1)
            nc = cur_c + dc[i] * (d - 1)
            break
        else:
          nr = cur_r + dr[i] * (d - 1)
          nc = cur_c + dc[i] * (d - 1)
          break
      if visit[nr][nc]: continue
      visit[nr][nc] = True
      que.append((nr, nc, dist + 1))
  return -1