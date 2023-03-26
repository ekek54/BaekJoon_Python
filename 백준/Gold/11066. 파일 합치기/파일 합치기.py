import sys
from math import inf
T = int(sys.stdin.readline())


def top_down(a, b, sizes, dp):
  if a == b:
    dp[a][b] = 0
    return 0
  if dp[a][b] != inf:
    return dp[a][b]
  for i in range(a, b):
    dp[a][b] = min(dp[a][b], top_down(a, i, sizes, dp) + top_down(i + 1, b, sizes, dp))
  dp[a][b] += sum(sizes[a: b + 1])
  return dp[a][b]


def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')

for _ in range(T):
  K = int(sys.stdin.readline())
  dp = [[inf for j in range(K)] for i in range(K)]
  sizes = list(map(int, sys.stdin.readline().split()))
  print(top_down(0, K - 1, sizes, dp))
  #pb(dp)