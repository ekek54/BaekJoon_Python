import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    adj_list[A].append(B)
    adj_list[B].append(A)
for adj in adj_list:
    adj.sort()
S, E = map(lambda x: int(x) - 1, sys.stdin.readline().split())
dist = [0 for _ in range(N)]
visit = [False for _ in range(N)]
pre = [i for i in range(N)]
visit[S] = True
que = deque()
que.append(S)
while que:
    cur = que.popleft()
    if cur == E: break
    for nxt in adj_list[cur]:
        if visit[nxt]: continue
        dist[nxt] = dist[cur] + 1
        pre[nxt] = cur
        visit[nxt] = True
        que.append(nxt)
go = dist[E]
#돌아오는 길
dist = [0 for _ in range(N)]
visit = [False for _ in range(N)]
i = E
while pre[i] != S:
    visit[pre[i]] = True
    i = pre[i]
que = deque()
que.append(E)
visit[E] = True
while que:
    cur = que.popleft()
    if cur == S: break
    for nxt in adj_list[cur]:
        if visit[nxt]: continue
        dist[nxt] = dist[cur] + 1
        visit[nxt] = True
        que.append(nxt)
come = dist[S]
print(go + come)