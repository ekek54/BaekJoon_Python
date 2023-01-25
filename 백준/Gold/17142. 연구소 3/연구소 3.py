import sys
from collections import deque
from math import inf

ans = inf
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
virus_rc_list = []
for i in range(N):
  for j in range(N):
    if board[i][j] == 2:
      virus_rc_list.append([i, j])

active_virus = []


def dfs(cnt):
  global ans
  if cnt == M:
    time = check(active_virus)
    if time != -1:
      ans = min(ans, time)
    return

  for i in range(len(virus_rc_list)):
    if active_virus and active_virus[-1] >= i:
      continue
    active_virus.append(i)
    dfs(cnt + 1)
    active_virus.pop()


def check(active_virus):
  dr = [1, -1, 0, 0]
  dc = [0, 0, 1, -1]
  time_board = [[0 for j in range(N)] for i in range(N)]
  visit = [[False for j in range(N)] for i in range(N)]
  que = deque()
  done_time = 0
  for i in range(M):
    r, c = virus_rc_list[active_virus[i]]
    visit[r][c] = True
    que.append([r, c])

  while que:
    cur_r, cur_c = que.popleft()
    #print(cur_r, cur_c)
    for i in range(4):
      nr = cur_r + dr[i]
      nc = cur_c + dc[i]
      if 0 <= nc < N and 0 <= nr < N:
        if not visit[nr][nc] and board[nr][nc] != 1:
          que.append([nr, nc])
          time_board[nr][nc] = time_board[cur_r][cur_c] + 1
          visit[nr][nc] = True

  for i in range(N):
    for j in range(N):
      if board[i][j] == 0 and time_board[i][j] == 0:
        return -1
      if board[i][j] == 2 and time_board[i][j] != 0:
        continue
      done_time = max(done_time, time_board[i][j])

  return done_time


dfs(0)
print(-1 if ans == inf else ans)
