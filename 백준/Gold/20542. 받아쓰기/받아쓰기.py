import sys
from math import inf

n, m = map(int, sys.stdin.readline().split())
A = " " + sys.stdin.readline().rstrip()
B = " " + sys.stdin.readline().rstrip()
DP = [[inf for j in range(m + 1)] for i in range(n + 1)]
for i in range(m + 1):
    DP[0][i] = i
for i in range(n + 1):
    DP[i][0] = i


for i in range(1, n + 1):
    for j in range(1, m + 1):
        candid = []
        if A[i] == B[j]:
            candid.append(DP[i - 1][j - 1])
        elif A[i] == 'i' and B[j] in "jl":
            candid.append(DP[i - 1][j - 1])
        elif A[i] == 'v' and B[j] in "w":
            candid.append(DP[i - 1][j - 1])
        else:
            candid.append(DP[i - 1][j - 1] + 1)
        candid.append(DP[i - 1][j] + 1)
        candid.append(DP[i][j - 1] + 1)
        DP[i][j] = min(candid)

def pb(board):
    for i in range(len(board)):
        print(board[i])
    print()
# pb(DP)
print(DP[n][m])



# print(A[-2])