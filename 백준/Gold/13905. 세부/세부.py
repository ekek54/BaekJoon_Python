import sys
import heapq
from math import inf

N, M = map(int, sys.stdin.readline().split())
s, e = map(int, sys.stdin.readline().split())
s -= 1
e -= 1
adj_list = [[] for _ in range(N)]
for _ in range(M):
  h1, h2, k = map(int, sys.stdin.readline().split())
  h1 -= 1
  h2 -= 1
  adj_list[h1].append((k, h2))  # 무게제한, 노드
  adj_list[h2].append((k, h1))

#print(adj_list)

def dijk(s, e):
  max_heap = []
  dist = [0 for _ in range(N)]
  # 힙에는 (-무게제한, 노드) 저장
  dist[s] = inf
  max_heap = [(-inf, s)]
  while max_heap:
    #print(max_heap)
    cur_k, cur_node = heapq.heappop(max_heap)
    cur_k = -cur_k
    #print(cur_k, cur_node)
    if cur_k < dist[cur_node]:
      continue
    for i in range(len(adj_list[cur_node])):
      nxt_node = adj_list[cur_node][i][1]
      nxt_dist = adj_list[cur_node][i][0]
      if dist[nxt_node] < min(dist[cur_node], nxt_dist):
        dist[nxt_node] = min(dist[cur_node], nxt_dist)
        heapq.heappush(max_heap, (-dist[nxt_node], nxt_node))
  return dist[e]


print(dijk(s, e))
