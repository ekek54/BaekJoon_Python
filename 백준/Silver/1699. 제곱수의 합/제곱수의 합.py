import sys
from math import inf

N = int(sys.stdin.readline())
dp = [inf for _ in range(N + 1)]
dp[0] = 0
dp[1] = 1
for i in range(1, N + 1):
  for j in range(int(i ** (1 / 2) + 1)):
    dp[i] = min(dp[i], dp[i - j ** 2] + 1)
print(dp[N])