import sys
from collections import deque

boards = [[list(map(int, sys.stdin.readline().split())) for j in range(5)] for i in range(5)]
N = 5
candidate = []


# 2차원 배열 회전
def rotate(board, r):
  if r == 0:
    return [[board[i][j] for j in range(N)] for i in range(N)]
  if r == 1:
    return [[board[N - 1 - j][i] for j in range(N)] for i in range(N)]
  if r == 2:
    return [[board[N - 1 - i][N - 1 - j] for j in range(N)] for i in range(N)]
  if r == 3:
    return [[board[j][N - 1 - i] for j in range(N)] for i in range(N)]


# 판 미리 회전시켜두기
rotated_boards = [[rotate(boards[i], j) for j in range(4)] for i in range(N)]

board_stack = []
rotate_stack = []
answer = 130


def dfs(cnt):
  global answer
  if answer == 12:
    return
  if cnt == 5:
    answer = min(answer, bfs())
    return

  for i in range(N):
    if i in board_stack:
      continue
    board_stack.append(i)
    for j in range(4):
      rotate_stack.append(j)
      dfs(cnt + 1)
      rotate_stack.pop()
    board_stack.pop()


def whitin_range(a):
  return 0 <= a < N


def bfs():
  if answer == 12:
    return 12
  dr = [1, -1, 0, 0, 0, 0]
  dc = [0, 0, 1, -1, 0, 0]
  dz = [0, 0, 0, 0, 1, -1]

  visit = [[[False for j in range(N)] for i in range(N)] for k in range(N)]
  que = deque()
  map = [rotated_boards[board_stack[i]][rotate_stack[i]] for i in range(len(board_stack))]
  if map[0][0][0] == 0 or map[4][4][4] == 0:
    return 130
  distance = [[[0 for j in range(N)] for i in range(N)] for k in range(N)]
  que.append((0, 0, 0))
  visit[0][0][0] = True
  while que:
    cur_r, cur_c, cur_z = que.popleft()
    if cur_r == 4 and cur_c == 4 and cur_z == 4:
      break
    for i in range(6):
      nr = cur_r + dr[i]
      nc = cur_c + dc[i]
      nz = cur_z + dz[i]
      if whitin_range(nr) and whitin_range(nc) and whitin_range(nz):
        if not visit[nr][nc][nz] and map[nr][nc][nz] == 1:
          distance[nr][nc][nz] = distance[cur_r][cur_c][cur_z] + 1
          visit[nr][nc][nz] = True
          que.append((nr, nc, nz))
  #if distance[4][4][4] == 44:
    #print(distance)
  return distance[4][4][4] if distance[4][4][4] != 0 else 130


dfs(0)
print(answer if answer != 130 else -1)
