import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
que = deque()
nque = deque()
cheeze_cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            cheeze_cnt += 1
pre_cnt = cheeze_cnt
time = 0
que.append((0, 0))
visit = [[False for j in range(M)] for i in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
while cheeze_cnt:
    pre_cnt = cheeze_cnt
    time += 1
    while que:
        cur_r, cur_c = que.popleft()
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if visit[nr][nc]: continue
            if board[nr][nc] == 1:
                nque.append((nr, nc))
                visit[nr][nc] = True
                cheeze_cnt -= 1
            else:
                que.append((nr, nc))
                visit[nr][nc] = True
    que, nque = nque, que

print(time)
print(pre_cnt)