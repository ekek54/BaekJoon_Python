import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
F_rcs = []
for i in range(N):
    for j in range(M):
        if board[i][j] == "J":
            J_rc = (i, j)
            board[i][j] = 0
        if board[i][j] == "F":
            F_rcs.append((i, j))

que = deque()
que.append((J_rc, True))
for F_rc in F_rcs:
    que.append((F_rc, False))
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
answer = 0
escape = False
while que:
    cur_rc, is_J = que.popleft()
    cur_r, cur_c = cur_rc
    if is_J and board[cur_r][cur_c] == "F": continue
    if escape:
        break
    for i in range(4):
        nr = cur_r + dr[i]
        nc = cur_c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if board[nr][nc] == "#": continue
            if board[nr][nc] == "F": continue
            if board[cur_r][cur_c] == "F":
                board[nr][nc] = "F"
                que.append(((nr, nc), False))
            else:
                if board[nr][nc] != ".": continue
                board[nr][nc] = board[cur_r][cur_c] + 1
                que.append(((nr, nc), True))
        else:
            if board[cur_r][cur_c] != "F":
                answer = board[cur_r][cur_c] + 1
                escape = True
                break
def pb(board):
    for i in range(len(board)):
        print(board[i])
    print('')
#pb(board)
print(answer if answer else "IMPOSSIBLE")