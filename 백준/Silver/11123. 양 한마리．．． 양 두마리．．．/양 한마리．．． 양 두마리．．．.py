import sys
from collections import deque

T = int(sys.stdin.readline())
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for _ in range(T):
    answer = 0
    que = deque()
    H, W = map(int, sys.stdin.readline().split())
    board = [sys.stdin.readline() for i in range(H)]
    visit = [[False for j in range(W)] for i in range(H)]
    for i in range(H):
        for j in range(W):
            if visit[i][j]: continue
            if board[i][j] == '.': continue
            que.append((i, j))
            visit[i][j] = True
            answer += 1
            while que:
                cur_r, cur_c = que.popleft()
                for k in range(4):
                    nr = cur_r + dr[k]
                    nc = cur_c + dc[k]
                    if not(0 <= nr < H and 0 <= nc < W): continue
                    if visit[nr][nc]: continue
                    if board[nr][nc] == '.': continue
                    que.append((nr, nc))
                    visit[nr][nc] = True
    print(answer)