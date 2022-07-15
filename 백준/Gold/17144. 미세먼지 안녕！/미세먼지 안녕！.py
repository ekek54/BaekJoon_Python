import sys
import copy

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
R, C, T = map(int,sys.stdin.readline().split())
room = [list(map(int,sys.stdin.readline().split())) for _ in range(R)]

def dust(board):
    org=copy.deepcopy(board)
    for i in range(R):
        for j in range(C):
            if board[i][j]>=5:
                move_dust=org[i][j]//5
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if 0<=nr<R and 0<=nc<C and board[nr][nc] != -1:
                        board[nr][nc] += move_dust
                        board[i][j] -= move_dust
    return

def spin(board,r,c,clock):
    di = [(0, 1), (-1, 0), (0, -1), (1, 0)] if clock else [(0, 1), (1, 0), (0, -1), (-1, 0)]
    tmp=0
    idx=0
    while 1:
        nr = r + di[idx][0]
        nc = c + di[idx][1]
        if 0 <= nr < R and 0 <= nc < C:
            if board[nr][nc] == -1:
                break
            board[nr][nc], tmp = tmp, board[nr][nc]
            r, c = nr, nc
        else:
            idx+=1
    return


def air(board):
    for i in range(R):
        if board[i][0] == -1:
            ac_top = (i,0)
            ac_bottom = (i+1,0)
            break
    spin(board, *ac_top, True)
    spin(board, *ac_bottom, False)
    return

while T>0:
    dust(room)
    air(room)
    T-=1

print(sum(map(sum,room))+2)