import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
adj_list = [[] for _ in range(N)]
indegree = [0 for _ in range(N)]
cnt = [0 for _ in range(N)]
cnt[-1] = 1
basic_idx_list = []
for _ in range(M):
    X, Y, K = map(int, sys.stdin.readline().split())
    X -= 1
    Y -= 1
    adj_list[X].append((Y, K))
    indegree[Y] += 1

for i in range(N):
    if len(adj_list[i]) == 0:
        basic_idx_list.append(i)

que = deque()
que.append(N - 1)
while que:
    cur_node = que.popleft()
    for nxt in adj_list[cur_node]:
        nxt_node, req_cnt = nxt
        indegree[nxt_node] -= 1
        cnt[nxt_node] += req_cnt * cnt[cur_node]
        if indegree[nxt_node] == 0:
            que.append(nxt_node)

for basic_idx in basic_idx_list:
    print(basic_idx + 1, cnt[basic_idx])