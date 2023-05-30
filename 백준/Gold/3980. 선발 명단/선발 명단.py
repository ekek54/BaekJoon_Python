import sys

C = int(sys.stdin.readline())
visit = [False for i in range(11)]
stack = []


def dfs(cnt, abils):
    result = 0
    if cnt == 11:
        for i in range(11):
            result += abils[i][stack[i]]
        return result

    for i in range(11):
        if visit[i]: continue
        if abils[cnt][i] == 0: continue
        visit[i] = True
        stack.append(i)
        result = max(result, dfs(cnt + 1, abils))
        stack.pop()
        visit[i] = False

    return result


for _ in range(C):
    abils = [list(map(int, sys.stdin.readline().split())) for _ in range(11)]
    print(dfs(0, abils))
