import sys
from collections import deque
from copy import deepcopy


def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')


N, Q = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(2 ** N)]
levels = list(map(int, sys.stdin.readline().split()))


def rotate90(board):
  N = len(board)
  M = len(board[0])
  return [[board[N - 1 - j][i] for j in range(N)] for i in range(M)]


def rotate_sub_board(r1, c1, r2, c2):
  global board
  sub_board = [[board[i][j] for j in range(c1, c2)] for i in range(r1, r2)]
  rotated_sub_board = rotate90(sub_board)
  for i in range(r1, r2):
    for j in range(c1, c2):
      board[i][j] = rotated_sub_board[i - r1][j - c1]


# 회전
def tornado(level):
  for i in range(2 ** (N - level)):
    for j in range(2 ** (N - level)):
      rotate_sub_board(2 ** level * i, 2 ** level * j, 2 ** level * (i + 1), 2 ** level * (j + 1))


# 얼음 녹이기
def fire():
  dr = [1, -1, 0, 0]
  dc = [0, 0, 1, -1]
  melts = []
  for i in range(2 ** N):
    for j in range(2 ** N):
      if board[i][j] == 0:
        continue
      adj_cnt = 0
      for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        if 0 <= nr < 2 ** N and 0 <= nc < 2 ** N:
          if board[nr][nc] > 0:
            adj_cnt += 1
      if adj_cnt < 3:
        melts.append((i, j))
  for rc in melts:
    r, c, = rc
    board[r][c] -= 1


def maximu_group_size():
  dr = [1, -1, 0, 0]
  dc = [0, 0, 1, -1]
  visit = [[False for j in range(2 ** N)] for i in range(2 ** N)]
  que = deque()
  result = 0
  for i in range(2 ** N):
    for j in range(2 ** N):
      if not visit[i][j] and board[i][j] != 0:
        group = []
        group.append((i, j))
        que.append((i, j))
        visit[i][j] = True
        while que:
          cur_r, cur_c = que.popleft()
          for k in range(4):
            nr = cur_r + dr[k]
            nc = cur_c + dc[k]
            if 0 <= nr < 2 ** N and 0 <= nc < 2 ** N:
              if not visit[nr][nc] and board[nr][nc] != 0:
                group.append((nr, nc))
                que.append((nr, nc))
                visit[nr][nc] = True
        result = max(result, len(group))
  return result


for level in levels:
  tornado(level)
  fire()

print(sum(map(sum, board)))
print(maximu_group_size())
