import sys

S = sys.stdin.readline().rstrip()
N = len(S)
M = int(sys.stdin.readline())
A = {}
for _ in range(M):
  a, x = sys.stdin.readline().split()
  A[a] = int(x)
dp = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
  dp[i] = dp[i - 1] + 1
  for j in range(i):
    sub_str = S[j: i]
    if S[j: i] in A:
      dp[i] = max(dp[i], dp[j] + A[sub_str])
print(dp[-1])