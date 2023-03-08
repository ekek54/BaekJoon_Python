import sys
from collections import deque

N = 8
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
walls = []

for i in range(N):
  for j in range(N):
    if board[i][j] == '#':
      walls.append((i, j))

wook_rc = (7, 0)
dr = [-1, -1, 0, 1, 1, 1, 0, -1, 0]
dc = [0, 1, 1, 1, 0, -1, -1, -1, 0]
que = deque()
que.append((wook_rc, 0))
answer = 0
while que:
  cur_rc, turn = que.popleft()
  if (0, 7) == cur_rc:
    answer = 1
    break
  cur_walls = [(wall[0] + turn, wall[1]) for wall in walls]
  nxt_walls = [(wall[0] + turn + 1, wall[1]) for wall in walls]
  cur_board = [['.' for j in range(8)] for i in range(8)]
  nxt_board = [['.' for j in range(8)] for i in range(8)]
  for cur_wall in cur_walls:
    r, c = cur_wall
    if 0 <= r < N and 0 <= c < N:
      cur_board[r][c] = '#'
  for nxt_wall in nxt_walls:
    r, c = nxt_wall
    if 0 <= r < N and 0 <= c < N:
      nxt_board[r][c] = '#'
  cur_r, cur_c = cur_rc

  for i in range(9):
    nr = cur_r + dr[i]
    nc = cur_c + dc[i]
    if 0 <= nr < N and 0 <= nc < N and cur_board[nr][nc] == '.' and nxt_board[nr][nc] == '.':
      que.append(((nr, nc), turn + 1))
print(answer)
