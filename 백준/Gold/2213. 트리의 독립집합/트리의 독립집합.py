import sys

n = int(sys.stdin.readline())
w = list(map(int, sys.stdin.readline().split()))
adj_list = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    adj_list[a].append(b)
    adj_list[b].append(a)

visit = [False for _ in range(n)]
dp = [[0, w[i]] for i in range(n)]
dp_pre = [[set([]), {i}] for i in range(n)]


def dfs(node):
    visit[node] = True
    for nxt in adj_list[node]:
        if visit[nxt]: continue
        dfs(nxt)
        if dp[nxt][0] <= dp[nxt][1]:
            dp[node][0] += dp[nxt][1]
            dp_pre[node][0] |= dp_pre[nxt][1]
        else:
            dp[node][0] += dp[nxt][0]
            dp_pre[node][0] |= dp_pre[nxt][0]
        dp[node][1] += dp[nxt][0]
        dp_pre[node][1] |= dp_pre[nxt][0]

dfs(0)
print(max(dp[0]))
answer_set = dp_pre[0][0] if dp[0][0] > dp[0][1] else dp_pre[0][1]
answer_set = list(answer_set)
answer_set.sort()
# answer_set = map(lambda x: x + 1, answer_set)
print(*map(lambda x: x + 1, answer_set))