import sys
from math import inf

N = int(sys.stdin.readline())
times = []
prices = []
dp = [0 for _ in range(N)]
for _ in range(N):
  t, p = map(int, sys.stdin.readline().split())
  times.append(t)
  prices.append(p)

for i in range(N):
  t = times[i]
  p = prices[i]
  dp[i] = max(dp[i], dp[i - 1])
  if i + t - 1 >= N:
    continue
  if i - 1 < 0:
    dp[i + t - 1] = max(dp[i + t - 1], p)
  else:
    dp[i + t - 1] = max(dp[i + t - 1], p + dp[i - 1])

print(dp[-1])
