import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
que = deque()

dist = [[-1 for j in range(m)] for i in range(n)]
visit = [[False for j in range(m)] for i in range(n)]

break_flag = False
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            que.append((i, j))
            dist[i][j] = 0
            visit[i][j] = True
            break_flag = True
        elif board[i][j] == 0:
            dist[i][j] = 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

while que:
    cur_r, cur_c = que.popleft()

    for i in range(4):
        nr = cur_r + dr[i]
        nc = cur_c + dc[i]
        if not (0 <= nr < n and 0 <= nc < m): continue
        if visit[nr][nc]: continue
        if board[nr][nc] == 0: continue
        que.append((nr, nc))
        dist[nr][nc] = dist[cur_r][cur_c] + 1
        visit[nr][nc] = True

def pb(board):
    for i in range(len(board)):
        print(*board[i])

pb(dist)