import sys
N = int(sys.stdin.readline())
dp = [[-1 for j in range(9)] for i in range(N)]
rice_cakes = []
for _ in range(N):
  arr = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
  m = arr[0]
  arr = arr[1:]
  rice_cakes.append(arr)

for i in range(len(rice_cakes[0])):
  dp[0][rice_cakes[0][i]] = 0

for i in range(1, N):
  for j in rice_cakes[i]:
    for k in rice_cakes[i - 1]:
      if dp[i - 1][k] == -1: continue
      if j == k: continue
      dp[i][j] = k
      break

def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')
#pb(dp)

answer = []

for i in rice_cakes[-1]:
  if dp[-1][i] != -1:
    answer.append(i + 1)
    nxt = dp[N - 1][i]
    idx = N - 2
    break

if not answer:
  print(-1)
else:
  while idx >= 0:
    answer.append(nxt + 1)
    nxt = dp[idx][nxt]
    idx -= 1
  print(*reversed(answer))

