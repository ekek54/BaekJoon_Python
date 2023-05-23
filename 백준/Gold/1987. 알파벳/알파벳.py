import sys

R, C = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(R)]
visit = [False for i in range(26)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
answer = 0

def char_idx(char):
    return ord(char) - 65

def dfs(r, c, cnt):
    global answer

    answer = max(answer, cnt)
    if answer == 26:
        return True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if not visit[char_idx(board[nr][nc])]:
                visit[char_idx(board[nr][nc])] = True
                if dfs(nr, nc, cnt + 1): return True
                visit[char_idx(board[nr][nc])] = False

visit[char_idx(board[0][0])] = True
dfs(0, 0, 1)
print(answer)