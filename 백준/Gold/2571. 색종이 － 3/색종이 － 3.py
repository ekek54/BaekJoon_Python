import sys
from math import inf


def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')


M = 100
N = int(sys.stdin.readline())
board = [[0 for j in range(M)] for i in range(M)]
acc_board = [[0 for j in range(M + 1)] for i in range(M + 1)]

for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  for i in range(b, b + 10):
    for j in range(a, a + 10):
      board[i][j] = 1

for i in range(M):
  acc = 0
  for j in range(M):
    acc += board[i][j]
    acc_board[i + 1][j + 1] = acc

for i in range(M + 1):
  acc = 0
  for j in range(M + 1):
    acc += acc_board[j][i]
    acc_board[j][i] = acc


def calc_part_sum(a, b):
  r1, c1 = a
  r2, c2 = b
  return acc_board[r2][c2] - acc_board[r2][c1] - acc_board[r1][c2] + acc_board[r1][c1]

answer = 0

for i in range(1, M + 1):
  for j in range(1, M + 1):
    for k in range(i):
      for l in range(j):
        partial_sum = calc_part_sum((k, l), (i, j))
        #print(partial_sum)
        if (i - k) * (j - l) == partial_sum:
          answer = max(answer, partial_sum)

print(answer)
