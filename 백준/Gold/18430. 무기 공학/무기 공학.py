import sys
from math import inf


def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dv = {'c': (0, 0), 'l': (0, -1), 'r': (0, 1), 'u': (-1, 0), 'd': (1, 0)}
case = [('l', 'd'), ('l', 'u'), ('u', 'r'), ('d', 'r')]
visit_board = [[0 for j in range(M)] for i in range(N)]
strength = 0
answer = 0

def dfs(cnt):
  global strength
  global answer
  if cnt == N * M:
    answer = max(answer, strength)
    return

  cur_r = cnt // M
  cur_c = cnt % M

  # 사용하지 않는 경우
  dfs(cnt + 1)

  # 사용하는 경우
  if visit_board[cur_r][cur_c] == 0:
    for i in range(4):
      can_visit = True
      for dir in case[i]:
        nr = cur_r + dv[dir][0]
        nc = cur_c + dv[dir][1]
        if nr < 0 or N <= nr or nc < 0 or M <= nc:
          can_visit = False
          break
        if visit_board[nr][nc] == 1:
          can_visit = False
          break
      if not can_visit: continue
      tmp_str = 0
      for dir in case[i]:
        nr = cur_r + dv[dir][0]
        nc = cur_c + dv[dir][1]
        visit_board[nr][nc] = 1
        tmp_str += board[nr][nc]
      visit_board[cur_r][cur_c] = 1
      tmp_str += board[cur_r][cur_c] * 2
      strength += tmp_str
      dfs(cnt + 1)
      strength -= tmp_str
      for dir in case[i]:
        nr = cur_r + dv[dir][0]
        nc = cur_c + dv[dir][1]
        visit_board[nr][nc] = 0
      visit_board[cur_r][cur_c] = 0

dfs(0)
print(answer)