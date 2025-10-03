import sys
N, M=map(int,sys.stdin.readline().split(' '))
numlist=[i+1 for i in range(N)]
checklist=[False]*N
result=[]
def dfs(cnt):
    if cnt==M:
        print(*result)
        return
    for i in range(N):
        result.append(numlist[i])
        dfs(cnt+1)
        result.pop()

dfs(0)