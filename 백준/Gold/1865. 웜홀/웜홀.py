import sys
from math import inf


# 음수 사이클 여부 반환
def bf(V, edges, src, visit):
  dist = [inf for _ in range(V)]
  dist[src] = 0
  visit[src] = True
  for i in range(V):
    for edge in edges:
      cur, nxt, t = edge
      if dist[cur] != inf and dist[nxt] > dist[cur] + t:
        if i == V - 1:
          return True
        dist[nxt] = dist[cur] + t
        visit[nxt] = True
  return False


TC = int(sys.stdin.readline())
for _ in range(TC):
  N, M, W = map(int, sys.stdin.readline().split())
  visit = [False for i in range(N)]
  edges = []
  for __ in range(M):
    S, E, T = map(int, sys.stdin.readline().split())
    S -= 1
    E -= 1
    edges.append((S, E, T))
    edges.append((E, S, T))

  for __ in range(W):
    S, E, T = map(int, sys.stdin.readline().split())
    S -= 1
    E -= 1
    T = -T
    edges.append((S, E, T))

  answer = False
  for i in range(N):
    if visit[i]:continue
    if bf(N, edges, i, visit):
      answer = True
      break

  print('YES' if answer else 'NO') 