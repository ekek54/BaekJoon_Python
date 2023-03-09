import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
shape_map = [[-1 for j in range(M)] for i in range(N)]
visit = [[False for j in range(M)] for i in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
que = deque()


def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')


shape_cnt = 0
shape_size = 0
shape_sizes = []
for i in range(N):
  for j in range(M):
    if visit[i][j]: continue
    if board[i][j] == 1:
      que.append((i, j))
      visit[i][j] = True
      while que:
        cur_r, cur_c = que.popleft()
        shape_map[cur_r][cur_c] = shape_cnt
        shape_size += 1
        for k in range(4):
          nr = cur_r + dr[k]
          nc = cur_c + dc[k]
          if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc] and board[nr][nc] == 1:
            que.append((nr, nc))
            visit[nr][nc] = True
      shape_cnt += 1
      shape_sizes.append(shape_size)
      shape_size = 0

answer = 0
for i in range(N):
  for j in range(M):
    new_shape_size = 0
    adj_shape_set = set()
    if shape_map[i][j] == -1:
      for k in range(4):
        adj_r = i + dr[k]
        adj_c = j + dc[k]
        if 0 <= adj_r < N and 0 <= adj_c < M and shape_map[adj_r][adj_c] != -1:
          adj_shape_set.add(shape_map[adj_r][adj_c])
      for adj_shape in adj_shape_set:
        new_shape_size += shape_sizes[adj_shape]
      new_shape_size += 1
      answer = max(answer, new_shape_size)
print(answer)