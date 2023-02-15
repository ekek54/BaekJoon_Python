import sys
from collections import deque
from copy import deepcopy

def pb(board):
  for i in range(len(board)):
    print(board[i])

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, list(sys.stdin.readline().rstrip('\n')))) for _ in range(N)]
set_cnt = 0
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
days = -1
while set_cnt != 1:
  #pb(board)
  #print('')
  set_cnt = 0
  que = deque()
  nxt_board = deepcopy(board)
  visit = [[False for j in range(M)] for i in range(N)]
  for i in range(N):
    for j in range(M):
      if board[i][j] != 0 and not visit[i][j]:
        set_cnt += 1
        que.append((i, j))
        visit[i][j] = True
        while que:
          cur_r, cur_c = que.popleft()
          speed = board[cur_r][cur_c]
          # 퍼트리기
          for k in range(cur_r - speed, cur_r + speed + 1):
            for l in range(cur_c - speed, cur_c + speed + 1):
              if 0 <= k < N and 0 <= l < M:
                nxt_board[k][l] = max(nxt_board[k][l], speed)

          for k in range(4):
            nr = cur_r + dr[k]
            nc = cur_c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] and not visit[nr][nc]:
              que.append((nr, nc))
              visit[nr][nc] = True
  board = nxt_board
  days += 1
print(days)