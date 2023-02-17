import sys
from collections import deque
from copy import deepcopy

def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')
def rotate(r, board):
  N = len(board)
  M = len(board[0])
  if r == 0:
    return board
  if r == 3:
    return [[board[N - 1 - j][i] for j in range(N)] for i in range(M)]
  if r == 2:
    return [[board[N - 1 - i][M - 1 - j] for j in range(M)] for i in range(N)]
  if r == 1:
    return [[board[j][M - 1 - i] for j in range(N)] for i in range(M)]

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
out_sand = 0
MOVE_BOARD = [[0, 0, 2, 0, 0],
              [0, 10, 7, 1, 0],
              [5, 0, 0, 0, 0],
              [0, 10, 7, 1, 0],
              [0, 0, 2, 0, 0]]
# 좌, 하, 우, 상
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
di_moves = [rotate(i, MOVE_BOARD) for i in range(4)]


def move(r, c, di):
  global out_sand
  nr = r + dr[di]
  nc = c + dc[di]
  cur_sand = board[nr][nc]
  remain_sand = cur_sand
  for i in range(nr - 2, nr + 3):
    for j in range(nc - 2, nc + 3):
      move_sand = int((di_moves[di][i - (nr - 2)][j - (nc - 2)] / 100) * cur_sand)
      #print(move_sand)
      remain_sand -= move_sand
      if 0 <= i < N and 0 <= j < N:
        board[i][j] += move_sand
      else:
        out_sand += move_sand
  ar = nr + dr[di]
  ac = nc + dc[di]
  if 0 <= ar < N and 0 <= ac < N:
    board[ar][ac] += remain_sand
  else:
    out_sand += remain_sand
  board[nr][nc] = 0
  return (nr, nc)


r, c = N // 2, N // 2
cnt = 0
while r != 0 or c != 0:
  dist = cnt // 2 + 1
  di = cnt % 4
  for _ in range(dist):
    if r == 0 and c == 0:
      break
    r,c = move(r, c, di)
  cnt += 1
print(out_sand)