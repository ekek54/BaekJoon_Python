import sys
from math import inf

N, M = map(int, sys.stdin.readline().split())
adj_matrix = [[inf for j in range(N)] for i in range(N)]

for i in range(N):
  adj_matrix[i][i] = 0

for _ in range(M):
  a, b, t = map(int, sys.stdin.readline().split())
  a -= 1
  b -= 1
  adj_matrix[a][b] = min(t, adj_matrix[a][b])
K = int(sys.stdin.readline())
C = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))

for k in range(N):
  for i in range(N):
    for j in range(N):
      adj_matrix[i][j] = min(adj_matrix[i][k] + adj_matrix[k][j], adj_matrix[i][j])

def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')
#pb(adj_matrix)

w = [0 for _ in range(N)]
min_w = inf
for i in range(N):
  dist = [0 for _ in range(K)]
  for j in range(K):
    dist[j] = adj_matrix[C[j]][i] + adj_matrix[i][C[j]]
  #print(dist)
  w[i] = max(dist)
  min_w = min(min_w, w[i])
answer = []
for i in range(N):
  if w[i] == min_w:
    answer.append(i + 1)
print(*answer)