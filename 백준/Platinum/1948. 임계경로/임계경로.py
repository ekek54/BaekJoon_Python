import sys
import heapq
sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
adj_list= [[] for _ in range(n)]
for i in range(m):
    src, des, time = map(int, sys.stdin.readline().split())
    src -= 1
    des -= 1
    adj_list[src].append((des, time))

start, end = map(int, sys.stdin.readline().split())
start -= 1
end -= 1
pre_node = [[] for _ in range(n)]
dist = [0 for _ in range(n)]
pq = []
pq.append((0, start))
while pq:
    cur_t, cur_node = heapq.heappop(pq)
    cur_t = -cur_t
    if dist[cur_node] > cur_t:
        continue
    for adj in adj_list[cur_node]:
        nxt_node, t = adj
        if dist[nxt_node] <= dist[cur_node] + t:
            if dist[nxt_node] == dist[cur_node] + t:
                pre_node[nxt_node].append(cur_node)
            else:
                pre_node[nxt_node] = [cur_node]
                dist[nxt_node] = dist[cur_node] + t
                heapq.heappush(pq, (-dist[nxt_node], nxt_node))
# print(dist)
# print(pre_node)
visit = [False for _ in range(n)]
def cnt_edge(node):
    if visit[node]:
        return 0
    visit[node] = True
    result = len(pre_node[node])
    for nxt in pre_node[node]:
        result += cnt_edge(nxt)
    return result
print(dist[end])
print(cnt_edge(end))