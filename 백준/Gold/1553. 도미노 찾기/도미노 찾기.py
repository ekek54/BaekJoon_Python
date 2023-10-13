import sys

N = 8
M = 7

board = [list(map(int, list(sys.stdin.readline().rstrip()))) for i in range(N)]
visit = [[False for j in range(M)] for i in range(N)]
dominos = [ (i,j) for i in range(7) for j in range(7) if i <= j]

global answer
answer = 0

def dfs(cnt):
    global answer
    if cnt == 28:
        answer += 1
        return


    for i in range(N):
        for j in range(M):
            if visit[i][j]: continue
            if j + 1 >= M: continue
            if visit[i][j + 1]: continue
            a = min(board[i][j], board[i][j + 1])
            b = max(board[i][j], board[i][j + 1])
            if (a, b) == dominos[cnt]:
                visit[i][j] = True
                visit[i][j + 1] = True
                dfs(cnt + 1)
                visit[i][j] = False
                visit[i][j + 1] = False

    for i in range(N):
        for j in range(M):
            if visit[i][j]: continue
            if i + 1 >= N: continue
            if visit[i + 1][j]: continue
            a = min(board[i][j], board[i + 1][j])
            b = max(board[i][j], board[i + 1][j])
            if (a, b) == dominos[cnt]:
                visit[i][j] = True
                visit[i + 1][j] = True
                dfs(cnt + 1)
                visit[i][j] = False
                visit[i + 1][j] = False

dfs(0)
print(answer)