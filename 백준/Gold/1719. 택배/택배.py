import sys
from math import inf

n, m = map(int, sys.stdin.readline().split())
adj_matrix = [[inf for j in range(n)] for i in range(n)]
for i in range(n):
  adj_matrix[i][i] = 0

# i -> j 경로의 경유지
stopover = [[-1 for j in range(n)] for i in range(n)]
for i in range(n):
  stopover[i][i] = i


for _ in range(m):
  a, b, t = map(int, sys.stdin.readline().split())
  a -= 1
  b -= 1
  adj_matrix[a][b] = t
  adj_matrix[b][a] = t
  stopover[a][b] = b
  stopover[b][a] = a

# 플로이드-워셜
for k in range(n):
  for i in range(n):
    for j in range(n):
      if adj_matrix[i][j] > adj_matrix[i][k] + adj_matrix[k][j]:
        adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]
        stopover[i][j] = k

# i에서 j로의 경로에서 i 다음 경유지
def nxt_node(i, j):
  if stopover[i][j] == j:
    return j
  else:
    return nxt_node(i, stopover[i][j])

answer = [['-' for j in range(n)] for i in range(n)]

for i in range(n):
  for j in range(n):
    if i == j: continue
    answer[i][j] = nxt_node(i, j) + 1

for i in range(n):
  print(*answer[i])