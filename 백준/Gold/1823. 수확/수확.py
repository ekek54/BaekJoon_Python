from sys import stdin
from sys import setrecursionlimit

#setrecursionlimit(4000000)

N = int(stdin.readline())
values = [int(stdin.readline()) for _ in range(N)]
dp = [[-1 for j in range(N)] for i in range(N)]
for i in range(N):
  dp[i][i] = values[i]

acc_sums = [0]
acc = 0
for i in range(N):
  acc += values[i]
  acc_sums.append(acc)


def sub_sum(i, j):
  return acc_sums[j + 1] - acc_sums[i]


def top_down(i, j):
  if dp[i][j] != -1:
    return dp[i][j]
  dp[i][j] = max(top_down(i + 1, j), top_down(i, j - 1)) + sub_sum(i, j)
  return dp[i][j]


# print(top_down(0, N - 1))

for j in range(N):
  for i in reversed(range(j)):
    if dp[i][j] != -1:
      continue
    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) + sub_sum(i, j)

print(dp[0][N - 1])
