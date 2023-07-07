import sys
from math import inf

N, M = map(int, sys.stdin.readline().split())
adj_matrix = [[inf for j in range(N)] for i in range(N)]
for i in range(N):
    adj_matrix[i][i] = 0


for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    A -= 1
    B -= 1
    adj_matrix[A][B] = 1
    adj_matrix[B][A] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][k] + adj_matrix[k][j])

# print(adj_matrix)
min_cost = inf
min_A = 0
min_B = 0

def calc_cost(A, B):
    result = 0
    for i in range(N):
        result += min(adj_matrix[A][i], adj_matrix[B][i])
    return result

for i in range(N):
    for j in range(i + 1, N):
        tmp = calc_cost(i, j)
        if min_cost > tmp:
            min_cost = tmp
            min_A = i
            min_B = j
print(min_A + 1, min_B + 1, min_cost * 2)