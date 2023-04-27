import sys
from collections import deque

T = int(sys.stdin.readline())
for t in range(T):
  N, K = map(int, sys.stdin.readline().split())
  D = list(map(int, sys.stdin.readline().split()))
  adj_list = [[] for _ in range(N)]
  indegree = [0 for _ in range(N)]
  for _ in range(K):
    x, y = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    indegree[y] += 1
    adj_list[x].append(y)
  target = int(sys.stdin.readline()) - 1
  time = [0 for _ in range(N)]
  que = deque()
  for i in range(N):
    if indegree[i] == 0:
      que.append(i)
  while que:
    cur_node = que.popleft()
    time[cur_node] += D[cur_node]
    for nxt in adj_list[cur_node]:
      indegree[nxt] -= 1
      time[nxt] = max(time[nxt], time[cur_node])
      if indegree[nxt] == 0:
        que.append(nxt)
  print(time[target])