import sys
from math import inf

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[[inf for k in range(3)] for j in range(M)] for i in range(N)]
dr = [-1, -1, -1]
dc = [-1, 0, 1]
for i in range(M):
  for j in range(3):
    dp[0][i][j] = board[0][i]
for i in range(N):
  for j in range(M):
    for k in range(3):
      if 0 <= i + dr[k] < N and 0 <= j + dc[k] < M:
        for l in range(3):
          if k == l: continue
          dp[i][j][k] = min(dp[i][j][k], dp[i + dr[k]][j + dc[k]][l] + board[i][j])

def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')
#pb(dp)
print(min(map(min,dp[N - 1])))