import sys
from math import inf
n, m = map(int, sys.stdin.readline().split())
adj_matrix = [[inf for j in range(n)] for i in range(n)]
answer = [['-' for j in range(n)] for i in range(n)]
for _ in range(m):
    a, b, d = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    answer[a][b] = b
    answer[b][a] = a
    adj_matrix[a][b] = d
    adj_matrix[b][a] = d

for i in range(n):
    adj_matrix[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if adj_matrix[i][j] > adj_matrix[i][k] + adj_matrix[k][j]:
                adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]
                answer[i][j] = answer[i][k]

for i in range(n):
    for j in range(n):
        if answer[i][j] == '-': continue
        answer[i][j] += 1

def pb(board):
    for i in range(len(board)):
        print(*board[i])

pb(answer)