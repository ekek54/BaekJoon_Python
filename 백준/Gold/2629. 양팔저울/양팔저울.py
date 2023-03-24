import sys
from collections import deque

limit = 40001
N = int(sys.stdin.readline())
weights = [0] + list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
targets = list(map(int, sys.stdin.readline().split()))
dp = [[False for _ in range(limit)] for i in range(N + 1)]
dp[0][0] = True
for i in range(1, N + 1):
  for j in range(limit):
    if dp[i - 1][j]:
      dp[i][j] = True
      dp[i][abs(j - weights[i])] = True
      if j + weights[i] < limit:
        dp[i][j + weights[i]] = True

#print(dp)
print(*['Y' if dp[N][targets[i]] else 'N' for i in range(M)])
