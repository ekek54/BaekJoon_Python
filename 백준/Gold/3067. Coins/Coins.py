import sys

T = int(sys.stdin.readline())

for t in range(T):
  N = int(sys.stdin.readline())
  coins = list(map(int, sys.stdin.readline().split()))
  M = int(sys.stdin.readline())
  dp = [[0 for j in range(M + 1)] for i in range(N)]
  for i in range(M + 1):
    if i % coins[0] == 0:
      dp[0][i] = 1
  for i in range(1, N):
    for j in range(M + 1):
      idx = 0
      while j - (coins[i] * idx) >= 0:
        dp[i][j] += dp[i - 1][j - (coins[i] * idx)]
        idx += 1
  print(dp[N-1][M])
