# 트리의 지름 문제
import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
adj_list = [[] for _ in range(N)]
for i in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    adj_list[u].append(v)
    adj_list[v].append(u)

# 가장 멀리있는 노드와 거리를 반환
visit = [False for _ in range(N)]


def dfs(node, dist):
    result = [0, 0]
    for nxt in adj_list[node]:
        if visit[nxt]:
            continue
        visit[nxt] = True
        tmp = dfs(nxt, dist + 1)
        if result[1] < tmp[1]:
            result = tmp
        visit[nxt] = False

    if result[1] == 0:
        return [node, dist]
    return result


diameter = dfs(dfs(0, 0)[0], 0)[1]
print(diameter // 2 if diameter % 2 == 0 else diameter //2 + 1)
