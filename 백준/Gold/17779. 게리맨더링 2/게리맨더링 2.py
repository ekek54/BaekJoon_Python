import sys
from math import inf

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
minimum_gap = inf


def calc_gap(x, y, d1, d2):
  population_list = [0 for i in range(5)]
  for r in range(N):
    for c in range(N):
      if 0 <= r < x + d1 and 0 <= c <= y and r + c < x + y:
        population_list[0] += board[r][c]
      elif 0 <= r <= x + d2 and y < c < N and r - c < x - y:
        population_list[1] += board[r][c]
      elif x + d1 <= r < N and 0 <= c < y - d1 + d2 and r - c > x + d1 - (y - d1):
        population_list[2] += board[r][c]
      elif x + d2 < r < N and y - d1 + d2 <= c < N and r + c > x + d2 + y + d2:
        population_list[3] += board[r][c]
      else:
        population_list[4] += board[r][c]
  return max(population_list) - min(population_list) if 0 not in population_list else inf


def check(x, y):
  global minimum_gap
  for d1 in range(1, N):
    for d2 in range(1, N):
      if 1 <= x + d1 + d2 <= N and 1 <= y - d1 and y + d2 <= N:
        #print(x, y, d1, d2)
        minimum_gap = min(minimum_gap, calc_gap(x, y, d1, d2))


for x in range(N):
  for y in range(N):
    check(x, y)

print(minimum_gap)