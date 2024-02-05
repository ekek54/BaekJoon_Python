import sys
import heapq

N, M, K = map(int, sys.stdin.readline().split())
stations = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
adj_list = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    u -= 1
    v -= 1
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))
visit = [False for _ in range(N)]
answer = 0
pq = []
for station in stations:
    pq.append((0, station))


while pq:
    cur_dist, cur_node = heapq.heappop(pq)
    if visit[cur_node]: continue
    visit[cur_node] = True
    answer += cur_dist

    for adj in adj_list[cur_node]:
        adj_node, adj_dist = adj
        if visit[adj_node]: continue
        heapq.heappush(pq, (adj_dist, adj_node))

print(answer)
