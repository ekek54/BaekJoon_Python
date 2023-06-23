import sys
from collections import deque


def pb(board):
    for i in range(len(board)):
        print(board[i])
    print()


dr = [2, -2, -2, 2, 1, -1, -1, 1]
dc = [1, -1, 1, -1, 2, -2, 2, -2]
N, M, K, t = map(int, sys.stdin.readline().split())
molds = [tuple(map(lambda x: int(x) - 1, sys.stdin.readline().split())) for _ in range(M)]
inspects = {}
board_odd = [[0 for j in range(N)] for i in range(N)]
board_even = [[0 for j in range(N)] for i in range(N)]
que = deque()
for _ in range(K):
    r, c = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    inspects[(r, c)] = True

for mold in molds:
    r, c = mold
    # if mold in inspects:
    #     inspects[mold] = 0
    board_even[r][c] = 1
    que.append((r, c, 0))
answer = False
while que:
    cur = que.popleft()
    cur_r, cur_c, cur_t = cur
    if cur_t == 0:
        spread_cnt = 0
        for i in range(8):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                spread_cnt += 1
        if spread_cnt == 0: continue
    
    if (cur_r, cur_c) in inspects:
        if t % 2 == 0:
            if board_even[cur_r][cur_c]:
                answer = True
                break
        else:
            if board_odd[cur_r][cur_c]:
                answer = True
                break
    if cur_t == t: continue
    spread_cnt = 0
    for i in range(8):
        nr = cur_r + dr[i]
        nc = cur_c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            spread_cnt += 1
            if cur_t % 2 == 0:
                if board_odd[nr][nc]: continue
                board_odd[nr][nc] = 1
                que.append((nr, nc, cur_t + 1))
            else:
                if board_even[nr][nc]: continue
                board_even[nr][nc] = 1
                que.append((nr, nc, cur_t + 1))
print("YES" if answer else "NO")
