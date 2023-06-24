import sys
import heapq

N, T = map(int, sys.stdin.readline().split())
chapters = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 for j in range(T + 1)] for i in range(N)]
for i in range(N):
    for j in range(T + 1):
        if i == 0:
            if j < chapters[0][0]:
                dp[i][j] = 0
            else:
                dp[i][j] = chapters[0][1]
        elif j < chapters[i][0]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - chapters[i][0]] + chapters[i][1])
print(dp[N - 1][T])