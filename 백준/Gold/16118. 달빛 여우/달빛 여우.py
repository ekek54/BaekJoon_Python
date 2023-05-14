import sys
import heapq
from math import inf
N, M = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N)]

def fox():
    dist = [inf for _ in range(N)]
    dist[0] = 0
    pq = []
    heapq.heappush(pq, (0, 0))
    while pq:
        cur_dist, cur = heapq.heappop(pq)
        if dist[cur] < cur_dist: continue
        for adj in adj_list[cur]:
            nxt, nxt_dist = adj
            if dist[nxt] > cur_dist + nxt_dist:
                dist[nxt] = cur_dist + nxt_dist
                heapq.heappush(pq, (dist[nxt], nxt))
    return dist

def wolf():
    dist = [[inf, inf] for _ in range(N)]
    dist[0][1] = 0
    pq = []
    heapq.heappush(pq, (0, 0, 0))
    while pq:
        cur_dist, cur, turn_cnt = heapq.heappop(pq)
        if dist[cur][(turn_cnt + 1) % 2] < cur_dist: continue
        for adj in adj_list[cur]:
            nxt, nxt_dist = adj
            if turn_cnt % 2 == 0:
                nxt_dist /= 2
            else:
                nxt_dist *= 2
            if dist[nxt][turn_cnt % 2] > cur_dist + nxt_dist:
                dist[nxt][turn_cnt % 2] = cur_dist + nxt_dist
                heapq.heappush(pq, (dist[nxt][turn_cnt % 2], nxt, turn_cnt + 1))
    return list(map(min, dist))

for _ in range(M):
    a, b, d = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    adj_list[a].append((b, d))
    adj_list[b].append((a, d))

fox_dist = fox()
#print(fox_dist)
wolf_dist = wolf()
#print(wolf_dist)

answer = 0
for i in range(N):
    if fox_dist[i] < wolf_dist[i]:
        answer += 1
print(answer)
