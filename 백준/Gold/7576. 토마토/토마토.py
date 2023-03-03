import sys
from collections import deque

def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')

M, N = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
que = deque()
answer = 0
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
for i in range(N):
  for j in range(M):
    if box[i][j] == 1:
      que.append((i,j))
while que:
  cur_r, cur_c = que.popleft()
  answer = max(answer, box[cur_r][cur_c])
  for i in range(4):
    nr = cur_r + dr[i]
    nc = cur_c + dc[i]
    if 0 <= nr < N and 0 <= nc < M:
      if box[nr][nc] == 0:
        box[nr][nc] = box[cur_r][cur_c] + 1
        que.append((nr, nc))
def is_done(box):
  for i in range(len(box)):
    for j in range(len(box[0])):
      if box[i][j] == 0:
        return False
  return True
print(answer - 1 if is_done(box) else -1)