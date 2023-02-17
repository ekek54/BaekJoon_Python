import sys
from math import inf
import copy

N = int(sys.stdin.readline())
RGB_costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
candidates = []
for i in range(3):
  dp = copy.deepcopy(RGB_costs)
  dp[0][i] = inf
  for j in range(1, N):
    dp[j][0] += min(dp[j - 1][1], dp[j - 1][2])
    dp[j][1] += min(dp[j - 1][0], dp[j - 1][2])
    dp[j][2] += min(dp[j - 1][0], dp[j - 1][1])
  #print(dp)
  #print(dp[-1][i])
  candidates.append(dp[-1][i])
print(min(candidates))