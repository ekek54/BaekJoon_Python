import sys
from collections import deque

def pb(board):
    for i in range(len(board)):
        print(board[i])
    print('')

N = sys.stdin.readline().rstrip()
M = len(N)
dp = [[-1 for j in range(M)] for i in range(M)]
for i in range(M):
    dp[i][i] = 1

def top_down(i, j):
    #print(i, j)
    if dp[i][j] != -1:
        return dp[i][j]

    if N[i + 1: j + 1] == N[i : j] and N[i] == N[j]:
        dp[i][j] = top_down(i + 1, j)
    else:
        dp[i][j] = top_down(i + 1, j) + top_down(i, j - 1)
    return dp[i][j]

print(top_down(0, M - 1))
#pb(dp)