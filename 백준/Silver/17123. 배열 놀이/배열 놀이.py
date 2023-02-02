import sys

T = int(sys.stdin.readline())
for t in range(T):
  N, M = map(int, sys.stdin.readline().split())
  A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
  row_sum = list(map(sum, A))
  col_sum = [sum([A[j][i] for j in range(N)]) for i in range(N)]
  for _ in range(M):
    r1, c1, r2, c2, v = map(int, sys.stdin.readline().split())
    for i in range(r1 - 1, r2):
      row_sum[i] += (c2 - c1 + 1) * v
    for i in range(c1 - 1, c2):
      col_sum[i] += (r2 - r1 + 1) * v
  print(*row_sum)
  print(*col_sum)