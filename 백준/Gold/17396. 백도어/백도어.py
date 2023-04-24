import sys
import heapq
from math import inf

N, M = map(int, sys.stdin.readline().split())
is_visible = list(map(int, sys.stdin.readline().split()))
is_visible[-1] = 0
adj_list = [[] for _ in range(N)]
pq = []
for _ in range(M):
  a, b, t = map(int, sys.stdin.readline().split())
  if is_visible[a] or is_visible[b]: continue
  adj_list[a].append((b, t))
  adj_list[b].append((a, t))


#print(adj_list)
dist = [inf for _ in range(N)]
dist[0] = 0
heapq.heappush(pq, (0, 0))
while pq:
  cur_dist, cur_node = heapq.heappop(pq)
  if cur_dist > dist[cur_node]:
    continue
  for nxt in adj_list[cur_node]:
    nxt_node, nxt_dist = nxt
    if dist[nxt_node] > cur_dist + nxt_dist:
      dist[nxt_node] = cur_dist + nxt_dist
      heapq.heappush(pq, (dist[nxt_node], nxt_node))
#print(dist)
print(dist[N - 1] if dist[N - 1] != inf else -1)