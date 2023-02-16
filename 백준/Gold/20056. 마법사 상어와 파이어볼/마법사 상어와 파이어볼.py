import sys
from math import floor

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, sys.stdin.readline().split())
board = [[[] for j in range(N)] for i in range(N)]
for i in range(M):
  r, c, m, s, d = map(int, sys.stdin.readline().split())
  board[r - 1][c - 1].append((m, s, d))

def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')

for _ in range(K):
  new_board = [[[] for j in range(N)] for i in range(N)]
  for i in range(N):
    for j in range(N):
      for fire_ball in board[i][j]:
        m, s, d = fire_ball
        nr = (i + s * dr[d]) % N
        nc = (j + s * dc[d]) % N
        new_board[nr][nc].append(fire_ball)
  for i in range(N):
    for j in range(N):
      if not len(new_board[i][j]) >= 2: continue
      new_m = floor(sum([new_board[i][j][k][0] for k in range(len(new_board[i][j]))]) / 5)
      new_s = floor(sum([new_board[i][j][k][1] for k in range(len(new_board[i][j]))]) / len(new_board[i][j]))
      if new_m > 0:
        if len(set([new_board[i][j][k][2] % 2 for k in range(len(new_board[i][j]))])) == 1:
          new_board[i][j] = [(new_m, new_s, 0), (new_m, new_s, 2), (new_m, new_s, 4), (new_m, new_s, 6)]
        else:
          new_board[i][j] = [(new_m, new_s, 1), (new_m, new_s, 3), (new_m, new_s, 5), (new_m, new_s, 7)]
      else:
        new_board[i][j] = []
  board = new_board
m_sum = 0
for i in range(N):
  for j in range(N):
    for fire_ball in board[i][j]:
      m, s, d = fire_ball
      m_sum += m

print(m_sum)
