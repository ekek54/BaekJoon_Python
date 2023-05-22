import sys

N, M, H = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
milk_rcs = [(0, 0)]
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            milk_rcs.append((i, j))
        if board[i][j] == 1:
            milk_rcs[0] = (i, j)

def dist(rc1, rc2):
    r1, c1 = rc1
    r2, c2 = rc2
    return abs(r1 - r2) + abs(c1 - c2)

stack = [0]
visit = [False for _ in range(len(milk_rcs))]
answer = 0
def dfs(cnt):
    #print(stack)
    global N, M, H, answer
    if len(stack) > 1 and stack[-1] == 0:
        answer = max(answer, len(stack) - 2)
        return

    for i in range(len(milk_rcs)):
        if visit[i]: continue
        if M < dist(milk_rcs[stack[-1]], milk_rcs[i]): continue
        M -= dist(milk_rcs[stack[-1]], milk_rcs[i])
        M += H
        visit[i] = True
        stack.append(i)
        dfs(cnt + 1)
        stack.pop()
        M += dist(milk_rcs[stack[-1]], milk_rcs[i])
        M -= H
        visit[i] = False


dfs(0)
print(answer)