import sys
from collections import deque


def pb(board):
    for i in range(N):
        print(board[i])
    print('')

count = 0
answer = 0
N, M, G, R = map(int, sys.stdin.readline().split())
garden = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
positive_grounds = []
for i in range(N):
    for j in range(M):
        if garden[i][j] == 2:
            positive_grounds.append((i, j))

visit = [False for _ in range(len(positive_grounds))]
green_grounds = []
green_stack = []
red_grounds = []
red_stack = []


def bfs():
    ret = 0
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    que = deque()
    # board의 원소: (상태, 시간)
    # 상태: 0: 방문 x, 1: 초록, 2: 빨강, 3: 꽃
    board = [[[0, 0] for j in range(M)] for i in range(N)]
    for green_ground in green_grounds:
        que.append(green_ground)
        g_r, g_c = green_ground
        board[g_r][g_c] = [1, 0]
    for red_ground in red_grounds:
        que.append(red_ground)
        r_r, r_c = red_ground
        board[r_r][r_c] = [2, 0]

    while que:
        #pb(board)
        cur_r, cur_c = que.popleft()
        if board[cur_r][cur_c][0] == 3: continue
        cur_color, cur_time = board[cur_r][cur_c]
        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                # 호수라면
                if garden[nr][nc] == 0: continue
                # 꽃이 피었다면
                if board[nr][nc][0] == 3: continue
                # 방문 x 라면
                if board[nr][nc][0] == 0:
                    board[nr][nc][0] = cur_color
                    board[nr][nc][1] = cur_time + 1
                    que.append((nr, nc))
                else:
                    if board[nr][nc][0] != cur_color and board[nr][nc][1] == cur_time + 1:
                        ret += 1
                        board[nr][nc][0] = 3
    return ret


def dfs_red(cnt):
    global answer
    global count
    if cnt == R:
        count += 1
        answer = max(answer, bfs())
        return

    for i in range(len(positive_grounds)):
        if visit[i]: continue
        if red_stack and red_stack[-1] >= i: continue
        red_stack.append(i)
        red_grounds.append(positive_grounds[i])
        visit[i] = True
        dfs_red(cnt + 1)
        red_stack.pop()
        red_grounds.pop()
        visit[i] = False

def dfs_green(cnt):
    if cnt == G:
        dfs_red(0)
        return

    for i in range(len(positive_grounds)):
        if visit[i]: continue
        if green_stack and green_stack[-1] >= i: continue
        green_stack.append(i)
        green_grounds.append(positive_grounds[i])
        visit[i] = True
        dfs_green(cnt + 1)
        green_stack.pop()
        green_grounds.pop()
        visit[i] = False

dfs_green(0)
print(answer)