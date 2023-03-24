import sys
from math import inf


def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')


N, M = map(int, sys.stdin.readline().split())
dist = [[inf for j in range(N)] for i in range(N)]
for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  a -= 1
  b -= 1
  dist[a][b] = 1
  dist[b][a] = 1

for i in range(N):
  dist[i][i] = 0

for k in range(N):
  for i in range(N):
    for j in range(N):
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
      
scores = list(map(sum, dist))
print(scores.index(min(scores)) + 1)
