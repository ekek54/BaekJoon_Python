import sys
from math import inf

N, M = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
dp = [[[-inf for k in range(M)] for j in range(N)] for i in range(N)]


def max_sub_sum(arr):
    ret = -inf
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            ret = max(ret, sum(arr[i:j]))
    return ret


def top_down(i, j, k):
    #print(i, j, k)
    if k == 0:
        dp[i][j][k] = max_sub_sum(arr[i: j + 1])
        return dp[i][j][k]
    if dp[i][j][k] != -inf:
        return dp[i][j][k]
    ret = -inf
    for l in range(i + 2 * (k - 1), j - 1):
        ret = max(top_down(i, l, k - 1) + top_down(l + 2, j, 0), ret)
    dp[i][j][k] = ret
    return ret

def pb(board):
    for i in range(len(board)):
        print(board[i])
    print('')


print(top_down(0, N - 1, M - 1))
#pb(dp)
