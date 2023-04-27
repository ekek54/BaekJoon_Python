import sys
from math import inf

s, N, K, R1, R2, C1, C2 = map(int, sys.stdin.readline().split())


def is_marked(r, c):
  for i in range(s):
    r_ = r // (N ** i)
    c_ = c // (N ** i)
    r__ = r_ % N
    c__ = c_ % N
    if (N - K) // 2 <= r__ < (N - K) // 2 + K and (N - K) // 2 <= c__ < (N - K) // 2 + K:
      return True
  return False


board = [['0' for j in range(C1, C2 + 1)] for i in range(R1, R2 + 1)]
for i in range(R1, R2 + 1):
  for j in range(C1, C2 + 1):
    if is_marked(i, j):
      board[i - R1][j - C1] = '1'

def pb(board):
  for i in range(len(board)):
    print(''.join(board[i]))
  print('')
pb(board)