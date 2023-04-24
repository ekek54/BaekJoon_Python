import sys
import heapq
from math import inf

N, M = map(int, sys.stdin.readline().split())
adj_list = [{} for _ in range(N)]
pq = []
for _ in range(M):
  a, b, c = map(int, sys.stdin.readline().split())
  a -= 1
  b -= 1
  if b in adj_list[a]:
    adj_list[a][b] = min(adj_list[a][b], c)
  else:
    adj_list[a][b] = c
  if a in adj_list[b]:
    adj_list[b][a] = min(adj_list[b][a], c)
  else:
    adj_list[b][a] = c


#print(adj_list)
dist = [inf for _ in range(N)]
dist[0] = 0
heapq.heappush(pq, (0, 0))
while pq:
  cur_dist, cur_node = heapq.heappop(pq)
  if cur_dist > dist[cur_node]:
    continue
  for nxt_node in adj_list[cur_node].keys():
    nxt_dist = adj_list[cur_node][nxt_node]
    if dist[nxt_node] > cur_dist + nxt_dist:
      dist[nxt_node] = cur_dist + nxt_dist
      heapq.heappush(pq, (dist[nxt_node], nxt_node))
#print(dist)
print(dist[N - 1])