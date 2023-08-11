import sys
from math import inf

N, M = map(int, sys.stdin.readline().split())
global answer
answer = inf
board = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

dc = [0, -1, 1]

dir_stack = []
cost_stack = []


def dfs(r, c):
    global answer

    if r == N - 1:
        # print(dir_stack)
        # print(cost_stack)
        # print()
        answer = min(answer, sum(cost_stack))
        return

    for i in range(3):
        if dir_stack and dir_stack[-1] == i: continue
        nc = c + dc[i]
        if 0 <= nc < M:
            dir_stack.append(i)
            cost_stack.append(board[r + 1][nc])
            dfs(r + 1, nc)
            cost_stack.pop()
            dir_stack.pop()

for i in range(M):
    dfs(-1,i)
print(answer)