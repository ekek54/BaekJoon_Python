import sys

N, M, K = map(int, sys.stdin.readline().split())


def rotate(board, r):
  N = len(board)
  M = len(board[0])
  if r == 0:
    return board
  elif r == 1:
    return [[board[N - 1 - i][j] for i in range(N)] for j in range(M)]
  elif r == 2:
    return [[board[N - 1 - i][M - 1 - j] for j in range(M)] for i in range(N)]
  elif r == 3:
    return [[board[i][M - 1 - j] for i in range(N)] for j in range(M)]


def check(board, sticker, start_i, start_j):
  R = len(sticker)
  C = len(sticker[0])
  arr = []
  if start_i + R > N or start_j + C > M:
    return False
  for i in range(R):
    for j in range(C):
      if sticker[i][j]:
        if board[start_i + i][start_j + j]:
          return False
        else:
          arr.append([start_i + i, start_j + j])
  for i in range(len(arr)):
    board[arr[i][0]][arr[i][1]] = 1
  return board


board = [[0 for j in range(M)] for i in range(N)]
for i in range(K):
  R, C = map(int, sys.stdin.readline().split())
  sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
  breaker = False
  for r in range(4):
    cur_sticker = rotate(sticker, r)
    # print(cur_sticker)
    for i in range(N):
      for j in range(M):
        check_res = check(board, cur_sticker, i, j)
        if check_res:
          # print(cur_sticker)
          board = check_res
          breaker = True
          break
      if breaker:
        break
    if breaker:
      break

print(sum(map(sum, board)))