from collections import deque

def solution(n, roads, sources, destination):
    adj_list = [[] for _ in range(n)]
    for road in roads:
        a, b = road
        a -= 1
        b -= 1
        adj_list[a].append(b)
        adj_list[b].append(a)
    def dfs(src):
        que = deque()
        visit = [False for _ in range(n)]
        dist = [-1 for _ in range(n)]
        que.append(src)
        visit[src] = True
        dist[src] = 0
        while que:
            cur = que.popleft()
            for nxt in adj_list[cur]:
                if not visit[nxt]:
                    visit[nxt] = True
                    dist[nxt] = dist[cur] + 1
                    que.append(nxt)
        return dist
    dist = dfs(destination - 1)
    return [dist[source - 1] for source in sources]