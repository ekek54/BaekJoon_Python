import sys
from math import inf

cases = set()
N, M = map(int, sys.stdin.readline().split())
woks = [0] + list(map(int, sys.stdin.readline().split()))

for i in range(M):
  for j in range(i + 1, M + 1):
    cases.add(woks[i] + woks[j])
dp = [inf for _ in range(N + 1)]
dp[0] = 0

for i in range(N + 1):
  for case in cases:
    if i - case >= 0:
      dp[i] = min(dp[i], dp[i - case] + 1)

print(dp[N] if dp[N] != inf else -1)