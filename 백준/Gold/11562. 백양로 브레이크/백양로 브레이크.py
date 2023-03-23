import sys
from math import inf

n, m = map(int, sys.stdin.readline().split())
adj_matrix = [[inf for j in range(n)] for i in range(n)]
for i in range(n):
  adj_matrix[i][i] = 0
for _ in range(m):
  u, v, b = map(int, sys.stdin.readline().split())
  u -= 1
  v -= 1
  adj_matrix[u][v] = 0
  if b == 0:
    adj_matrix[v][u] = 1
  else:
    adj_matrix[v][u] = 0

for k in range(n):
  for i in range(n):
    for j in range(n):
      adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][k] + adj_matrix[k][j])

k = int(sys.stdin.readline())
for _ in range(k):
  s, e = map(int, sys.stdin.readline().split())
  s -= 1
  e -= 1
  print(adj_matrix[s][e])
