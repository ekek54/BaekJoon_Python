import sys
from math import inf
import heapq

N, M, X, Y = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    adj_list[A].append((C, B))
    adj_list[B].append((C, A))


def dijk():
    pq = []
    dist = [inf for _ in range(N)]
    dist[Y] = 0
    heapq.heappush(pq, (0, Y))
    while pq:
        cur_dist, cur_node = heapq.heappop(pq)
        if dist[cur_node] < cur_dist:
            continue
        for nxt in adj_list[cur_node]:
            nxt_dist, nxt_node = nxt
            if dist[nxt_node] > cur_dist + nxt_dist:
                dist[nxt_node] = cur_dist + nxt_dist
                heapq.heappush(pq, (dist[nxt_node], nxt_node))
    #print(dist)
    return dist


dist = dijk()
dist.sort()
dist = list(map(lambda x: x * 2, dist))
answer = 1
acc = 0
for i in range(N):
    if dist[i] > X:
        answer = -1
        break
    if acc + dist[i] > X:
        acc = dist[i]
        answer += 1
    else:
        acc += dist[i]
print(answer)
