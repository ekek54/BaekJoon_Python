import sys

arr1 = sys.stdin.readline().rstrip()
arr2 = sys.stdin.readline().rstrip()
N = len(arr1)
M = len(arr2)
dp = [['' for j in range(M + 1)] for i in range(N + 1)]
for i in range(1, N + 1):
  for j in range(1, M + 1):
    if arr1[i - 1] == arr2[j - 1]:
      dp[i][j] = dp[i - 1][j - 1] + arr1[i - 1]
    else:
      if len(dp[i - 1][j]) > len(dp[i][j - 1]):
        dp[i][j] = dp[i - 1][j]
      else:
        dp[i][j] = dp[i][j - 1]


def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')

#pb(dp)
print(len(dp[N][M]))
print(dp[N][M])