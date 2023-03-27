import sys
from math import inf

N = int(sys.stdin.readline())
memo = [[inf for j in range(N)] for i in range(N)]

sizes = []
for i in range(N):
  a, b = map(int, sys.stdin.readline().split())
  sizes.append((a, b))


def top_down(i, j, sizes):
  if i == j: return 0
  if abs(i - j) == 1:
    return sizes[i][0] * sizes[i][1] * sizes[j][1]
  if memo[i][j] != inf:
    return memo[i][j]
  for k in range(i, j):
    memo[i][j] = min(memo[i][j],
                     top_down(i, k, sizes) + top_down(k + 1, j, sizes) + sizes[i][0] * sizes[k][1] * sizes[j][1])
  return memo[i][j]


print(top_down(0, N - 1, sizes))
