import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
visit = [False for _ in range(N)]
A.sort()
stack = []
ans_set = set()


def dfs(cnt):
    if cnt == M:
        ans_set.add(tuple(stack))
        return

    for i in range(N):
        if visit[i]: continue
        if stack and stack[-1] > A[i]: continue
        stack.append(A[i])
        visit[i] = True
        dfs(cnt + 1)
        stack.pop()
        visit[i] = False


dfs(0)
ans_list = list(ans_set)
ans_list.sort()
for ans in ans_list:
    print(*ans)
