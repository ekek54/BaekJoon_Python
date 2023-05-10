import sys
from collections import deque
N = int(sys.stdin.readline())
arr = []
dp = [1 for _ in range(N)]
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))