import sys

arr1 = sys.stdin.readline().rstrip()
arr2 = sys.stdin.readline().rstrip()
arr3 = sys.stdin.readline().rstrip()
N = len(arr1)
M = len(arr2)
O = len(arr3)
dp = [[[0 for k in range(O + 1)] for j in range(M + 1)] for i in range(N + 1)]
dx = [-1, -1, -1, 0, 0, 0]
dy = [-1, 0, 0, -1, -1, 0]
dz = [0, -1, 0, -1, 0, -1]
for i in range(1, N + 1):
  for j in range(1, M + 1):
    for k in range(1, O + 1):
      if arr1[i - 1] == arr2[j - 1] == arr3[k - 1]:
        dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
      else:
        dp[i][j][k] = max([dp[i + dx[l]][j + dy[l]][k + dz[l]] for l in range(6)])


print(dp[N][M][O])
