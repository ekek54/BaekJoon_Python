import sys
import heapq
from math import inf


N, M, A, B, C = map(int, sys.stdin.readline().split())
A -= 1
B -= 1
adj_list = [[] for _ in range(N)]

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    adj_list[a].append([b, c])
    adj_list[b].append([a, c])

pq = []
cost = [inf for _ in range(N)]
cost[A] = 0
shame = [inf for _ in range(N)]
shame[A] = 0
pq.append([0, 0, A])
while pq:
    cur_shame, cur_cost, cur_node = heapq.heappop(pq)
    if cur_cost > cost[cur_node] and cur_shame > shame[cur_node]: continue
    for adj in adj_list[cur_node]:
        nxt_node, nxt_cost = adj
        nxt_shame = max(cur_shame, nxt_cost)
        nxt_total = cur_cost + nxt_cost
        if nxt_total > C: continue
        if cost[nxt_node] > nxt_total and shame[nxt_node] > nxt_shame:
            heapq.heappush(pq, [nxt_shame, nxt_total, nxt_node])
            cost[nxt_node] = nxt_total
            shame[nxt_node] = nxt_shame
        elif cost[nxt_node] > nxt_total:
            heapq.heappush(pq, [nxt_shame, nxt_total, nxt_node])
            cost[nxt_node] = nxt_total
        elif shame[nxt_node] > nxt_shame:
            heapq.heappush(pq, [nxt_shame, nxt_total, nxt_node])
            shame[nxt_node] = nxt_shame
# print(cost)
# print(shame)
print(shame[B] if shame[B] != inf else -1)