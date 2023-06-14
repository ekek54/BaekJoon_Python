import sys
import heapq
from math import inf

N, M = map(int, sys.stdin.readline().split())
edges = {}
adj_list = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    if a > b:
        a, b = b, a
    edges[(a, b)] = t
    adj_list[a].append(b)
    adj_list[b].append(a)


def path(pre):
    result = []
    cur = N - 1
    while True:
        result.append(cur)
        if cur == pre[cur]: break
        cur = pre[cur]
    return list(reversed(result))


def dijk(xedge):
    pq = []
    dist = [inf for _ in range(N)]
    pre = [i for i in range(N)]
    dist[0] = 0
    heapq.heappush(pq, (0, 0))
    while pq:
        cur_dist, cur = heapq.heappop(pq)
        if dist[cur] < cur_dist: continue
        for nxt in adj_list[cur]:
            edge_key = tuple(sorted((cur, nxt)))
            if xedge == edge_key: continue
            nxt_dist = edges[edge_key]
            if dist[nxt] > cur_dist + nxt_dist:
                dist[nxt] = cur_dist + nxt_dist
                pre[nxt] = cur
                heapq.heappush(pq, (dist[nxt], nxt))
    # print(dist)
    return [dist[N - 1], path(pre)]


basic_dist, basic_path = dijk((0, 0))
# print(basic_dist)
# print(basic_path)
answer = 0
for i in range(len(basic_path) - 1):
    xedge = tuple(sorted((basic_path[i], basic_path[i + 1])))
    answer = max(answer, dijk(xedge)[0] - basic_dist)

print(answer if answer != inf else -1)
