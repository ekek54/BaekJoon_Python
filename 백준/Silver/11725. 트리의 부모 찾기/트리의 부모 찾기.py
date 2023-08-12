import sys
from collections import deque

N = int(sys.stdin.readline())
adj_list = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    adj_list[a].append(b)
    adj_list[b].append(a)

que = deque()
visit = [False for _ in range(N)]

que.append(0)
visit[0] = True
parent = [-1 for _ in range(N)]

while que:
    cur_node = que.popleft()
    for nxt in adj_list[cur_node]:
        if visit[nxt]: continue
        parent[nxt] = cur_node
        que.append(nxt)
        visit[nxt] = True

for i in range(1, N):
    print(parent[i] + 1)