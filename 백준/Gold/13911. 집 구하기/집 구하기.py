import sys
import heapq
from math import inf

V, E = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(V)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    adj_list[u].append((w, v))
    adj_list[v].append((w, u))
minus_one = lambda x: int(x) - 1
M, x = map(int, sys.stdin.readline().split())
macs = list(map(minus_one, sys.stdin.readline().split()))
S, y = map(int, sys.stdin.readline().split())
stars = list(map(minus_one, sys.stdin.readline().split()))

def dijk(srcs):
    dist_from_srcs = [inf for _ in range(V)]
    pq = []
    for src in srcs:
        dist_from_srcs[src] = 0
        heapq.heappush(pq, (0, src))
    while pq:
        cur_dist_from_srcs, cur_node = heapq.heappop(pq)
        if dist_from_srcs[cur_node] < cur_dist_from_srcs: continue
        for nxt in adj_list[cur_node]:
            dist_from_cur_to_nxt, nxt_node = nxt
            if dist_from_srcs[nxt_node] > dist_from_cur_to_nxt + cur_dist_from_srcs:
                dist_from_srcs[nxt_node] = dist_from_cur_to_nxt + cur_dist_from_srcs
                heapq.heappush(pq, (dist_from_srcs[nxt_node], nxt_node))
    return dist_from_srcs

dist_from_mac = dijk(macs)
dist_from_stars = dijk(stars)
#print(dist_from_mac)
#print(dist_from_stars)
answer = inf
for i in range(V):
    if dist_from_mac[i] == 0 or dist_from_stars[i] == 0: continue
    if dist_from_mac[i] <= x and dist_from_stars[i] <= y:
        answer = min(answer, dist_from_mac[i] + dist_from_stars[i])
print(answer if answer != inf else -1)