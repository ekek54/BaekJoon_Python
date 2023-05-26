import sys
from math import inf

V, E = map(int, sys.stdin.readline().split())
dist = [[inf for j in range(V)] for i in range(V)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    dist[a][b] = c

def pb(board):
    for i in range(len(board)):
        print(board[i])
    print('')
for k in range(V):
    for i in range(V):
        for j in range(V):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
answer = min(dist[i][i] for i in range(V))
print(answer if answer != inf else -1)
