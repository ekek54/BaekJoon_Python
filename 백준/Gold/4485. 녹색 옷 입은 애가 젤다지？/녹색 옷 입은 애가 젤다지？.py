import sys
from math import inf
import heapq

problem_num = 1
pq = []
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
while True:
  N = int(sys.stdin.readline())
  if N == 0:
    break
  board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
  dist = [[inf for j in range(N)] for i in range(N)]
  dist[0][0] = board[0][0]
  heapq.heappush(pq, (board[0][0], 0, 0))
  while pq:
    d, r, c = heapq.heappop(pq)
    if d > dist[r][c]:
      continue
    for i in range(4):
      nr = r + dr[i]
      nc = c + dc[i]
      if 0 <= nr < N and 0 <= nc < N:
        if dist[nr][nc] > d + board[nr][nc]:
          dist[nr][nc] = d + board[nr][nc]
          heapq.heappush(pq, (dist[nr][nc], nr, nc))
  print("Problem", str(problem_num) + ':', dist[N - 1][N - 1])
  problem_num += 1
