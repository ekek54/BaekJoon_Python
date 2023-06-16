import sys
sys.setrecursionlimit(10000)

N = int(sys.stdin.readline())
populations = list(map(int, sys.stdin.readline().split()))
adj_list = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    adj_list[a].append(b)
    adj_list[b].append(a)

visit = [False for _ in range(N)]
dp = [[0, populations[i]] for i in range(N)]


def dfs(node):
    nxts = []
    for adj in adj_list[node]:
        if visit[adj]: continue
        nxts.append(adj)

    if not nxts:
        dp[node][0] = 0
        dp[node][1] = populations[node]
        return

    for nxt in nxts:
        visit[nxt] = True
        dfs(nxt)
        dp[node][0] += max(dp[nxt])
        dp[node][1] += dp[nxt][0]
visit[0] = True
dfs(0)
print(max(dp[0]))