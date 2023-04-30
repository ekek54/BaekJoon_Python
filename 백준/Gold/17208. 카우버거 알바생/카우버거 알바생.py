import sys
from collections import deque
from math import inf

N, M, K = map(int, sys.stdin.readline().split())
order = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[[-1 for k in range(N + 1)] for j in range(K + 1)] for i in range(M + 1)]


def top_down(i, j, k):
  #print(i, j, k)
  if i < 0 or j < 0: return -1
  if k == 0: return 0


  if dp[i][j][k] != -1:
    return dp[i][j][k]

  ret = max(top_down(i - order[k - 1][0], j - order[k - 1][1], k - 1) + 1, top_down(i, j, k - 1))
  dp[i][j][k] = ret
  return ret

print(top_down(M, K, N))
#print(dp)

