import sys
import heapq
from math import inf

N, M, X = map(int, sys.stdin.readline().split())
X -= 1
in_adj_list = [[] for _ in range(N)]
out_adj_list = [[] for _ in range(N)]
for _ in range(M):
  a, b, t = map(int, sys.stdin.readline().split())
  a -= 1
  b -= 1
  out_adj_list[a].append((b, t))
  in_adj_list[b].append((a, t))


def dijk(adj_list):
  dist = [inf for _ in range(N)]
  pq = []
  dist[X] = 0
  pq.append((0, X))
  while pq:
    cur_dist, cur_node = heapq.heappop(pq)
    if cur_dist > dist[cur_node]:
      continue
    for nxt in adj_list[cur_node]:
      nxt_node, nxt_dist = nxt
      if dist[nxt_node] > cur_dist + nxt_dist:
        dist[nxt_node] = cur_dist + nxt_dist
        heapq.heappush(pq, (dist[nxt_node], nxt_node))
  return dist
to_X = dijk(in_adj_list)
to_home = dijk(out_adj_list)
round_trip = [to_X[i] + to_home[i] for i in range(N)]
print(max(round_trip))