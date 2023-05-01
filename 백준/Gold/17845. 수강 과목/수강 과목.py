import sys
from collections import deque
from math import inf

N, K = map(int, sys.stdin.readline().split())
importances = []
times = []
for _ in range(K):
  i, t = map(int, sys.stdin.readline().split())
  importances.append(i)
  times.append(t)

dp = [[0 for j in range(N + 1)] for i in range(K)]
for i in range(K):
  for j in range(N + 1):
    if j - times[i] >= 0:
      dp[i][j] = max(dp[i][j], dp[i - 1][j - times[i]] + importances[i])
    dp[i][j] = max(dp[i][j], dp[i - 1][j])

def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')

print(dp[K - 1][N])