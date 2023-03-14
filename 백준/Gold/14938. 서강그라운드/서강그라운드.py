import sys
from math import inf
n, m, r = map(int, sys.stdin.readline().split())
item_counts = list(map(int, sys.stdin.readline().split()))
answer = 0

adj_board = [[inf for j in range(n)] for i in range(n)]
for i in range(n):
  adj_board[i][i] = 0

for _ in range(r):
  a, b, l = map(int, sys.stdin.readline().split())
  a -= 1
  b -= 1
  adj_board[a][b] = l
  adj_board[b][a] = l

for k in range(n):
  for i in range(n):
    for j in range(n):
      adj_board[i][j] = min(adj_board[i][j], adj_board[i][k] + adj_board[k][j])

for i in range(n):
  item_cnt = 0
  for j in range(n):
    if adj_board[i][j] <= m:
      item_cnt += item_counts[j]
  answer = max(answer, item_cnt)
print(answer)