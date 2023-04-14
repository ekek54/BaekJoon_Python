import sys
import heapq

N, M = map(int, sys.stdin.readline().split())
adj_list = [{} for _ in range(N)]

for _ in range(M):
  A, B, C = map(int, sys.stdin.readline().split())
  A -= 1
  B -= 1
  if B in adj_list[A]:
    adj_list[A][B] = max(adj_list[A][B], C)
  else:
    adj_list[A][B] = C
  if A in adj_list[B]:
    adj_list[A][B] = max(adj_list[B][A], C)
  else:
    adj_list[B][A] = C

src, des = map(int, sys.stdin.readline().split())
src -= 1
des -= 1


def dijk(src, des):
  pq = []
  max_w_limit = [-1 for _ in range(N)]
  max_w_limit[src] = 1000000001
  pq.append((-1000000001, src))
  while pq:
    cur_max_w_limit, cur_island = heapq.heappop(pq)
    cur_max_w_limit = -cur_max_w_limit
    if max_w_limit[cur_island] > cur_max_w_limit:
      continue
    for nxt_island in adj_list[cur_island].keys():
      nxt_w_limit = adj_list[cur_island][nxt_island]
      if max_w_limit[nxt_island] < min(cur_max_w_limit, nxt_w_limit):
        max_w_limit[nxt_island] = min(cur_max_w_limit, nxt_w_limit)
        heapq.heappush(pq, (-max_w_limit[nxt_island], nxt_island))
  #print(max_w_limit)
  return max_w_limit[des]

print(dijk(src, des))