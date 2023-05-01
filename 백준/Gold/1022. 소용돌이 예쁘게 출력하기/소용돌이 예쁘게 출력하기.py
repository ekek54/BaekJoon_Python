import sys
from collections import deque
from math import inf

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())


def calc(r, c):
  #print(r, c)
  if r == 0 and c == 0: return 1
  if abs(r) >= abs(c):
    n = abs(r)
    if r < 0:
      k = 3
      ret = 4 * (n ** 2) + (k - 4) * n + 1 - c
    else:
      k = 7
      ret = 4 * (n ** 2) + (k - 4) * n + 1 + c
  else:
    n = abs(c)
    if c < 0:
      k = 5
      ret = 4 * (n ** 2) + (k - 4) * n + 1 + r
    else:
      k = 1
      ret = 4 * (n ** 2) + (k - 4) * n + 1 - r
  #print(ret)
  return ret


board = [[0 for j in range(c2 - c1 + 1)] for i in range(r2 - r1 + 1)]

for i in range(r1, r2 + 1):
  for j in range(c1, c2 + 1):
    board[i - r1][j - c1] = calc(i, j)


def pb(board):
  max_len = len(str(max(map(max, board))))
  for i in range(len(board)):
    str_nums = list(map(str, board[i]))
    for idx, str_num in enumerate(str_nums):
      str_nums[idx] = str_num.rjust(max_len, ' ')
    print(*str_nums)

pb(board)
