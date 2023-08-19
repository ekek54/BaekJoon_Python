import sys
from collections import deque

H, W = map(int, sys.stdin.readline().split())
input_int = lambda x: int(x) if x.isdigit() else 0
board = [list(map(input_int, list(sys.stdin.readline()))) for _ in range(H)]


def pb(board):
    for i in range(len(board)):
        print(board[i])
    print("")


# pb(board)

que = deque()
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
answer = 0

for i in range(H):
    for j in range(W):
        if board[i][j] == 0:
            que.append((i, j, 0))


def oob(r, c):
    return not (0 <= r < H and 0 <= c < W)


while que:
    r, c, cnt = que.popleft();
    answer = max(answer, cnt)

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]
        if oob(nr, nc): continue
        if board[nr][nc] == 0: continue
        board[nr][nc] -= 1
        if board[nr][nc] == 0:
            que.append((nr, nc, cnt + 1))

print(answer)