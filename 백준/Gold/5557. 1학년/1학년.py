from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp = [[0 for j in range(21)] for i in range(N - 1)]
visit = [[False for j in range(21)] for i in range(N - 1)]
dp[0][arr[0]] = 1
visit[0][arr[0]] = True

def top_down(i, j):
  #print(i, j)
  if i < 0: return 0
  if j < 0 or j > 20:
    return 0
  if visit[i][j]: return dp[i][j]
  dp[i][j] = top_down(i - 1, j - arr[i]) + top_down(i - 1, j + arr[i])
  visit[i][j] = True
  return dp[i][j]


print(top_down(N - 2, arr[-1]))
def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')

#pb(dp)