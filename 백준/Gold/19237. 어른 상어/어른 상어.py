import sys
import copy

N, M, K = map(int, sys.stdin.readline().split())
shark_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
sharks_di = list(map(int, sys.stdin.readline().split()))
sharks_prior = [[list(map(int, sys.stdin.readline().split())) for j in range(4)] for i in range(M)]
k = 0
smell_board = [[False for j in range(N)] for i in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def done():
  return sum(map(sum, shark_board)) == 1


def spread_smell():
  for i in range(N):
    for j in range(N):
      if shark_board[i][j]:
        shark_num = shark_board[i][j]
        smell_board[i][j] = [shark_num, K]


def isEmpty(r, c):
  return smell_board[r][c] == False


def mySmell(r, c, num):
  return smell_board[r][c][0] == num


def shark_move():
  global shark_board
  tmp_shark_board = [[0 for j in range(N)] for i in range(N)]
  for i in range(N):
    for j in range(N):
      if shark_board[i][j]:
        shark_num = shark_board[i][j]
        shark_di = sharks_di[shark_num - 1]
        shark_prior = sharks_prior[shark_num - 1][shark_di - 1]
        move_to_empty = False
        for di in shark_prior:
          nr = i + dr[di - 1]
          nc = j + dc[di - 1]
          if 0 <= nr < N and 0 <= nc < N:
            if isEmpty(nr, nc):
              move_to_empty = True
              if tmp_shark_board[nr][nc] == 0 or tmp_shark_board[nr][nc] > shark_num:
                tmp_shark_board[nr][nc] = shark_num
                sharks_di[shark_num - 1] = di
              break
        move_to_my_space = False
        if not move_to_empty:
          for di in shark_prior:
            nr = i + dr[di - 1]
            nc = j + dc[di - 1]
            if 0 <= nr < N and 0 <= nc < N:
              if mySmell(nr, nc, shark_num):
                move_to_my_space = True
                tmp_shark_board[nr][nc] = shark_num
                sharks_di[shark_num - 1] = di
                break
  shark_board = tmp_shark_board


def reduce_smell():
  for i in range(N):
    for j in range(N):
      if smell_board[i][j]:
        smell_board[i][j][1] -= 1
        if smell_board[i][j][1] == 0:
          smell_board[i][j] = False


def pb(board):
  for i in range(N):
    print(board[i])


while k <= 1000 and not done():
  k += 1
  spread_smell()
  shark_move()
  reduce_smell()

print(k if k <= 1000 else -1)
