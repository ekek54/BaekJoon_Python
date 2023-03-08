import sys
from collections import deque
sys.setrecursionlimit(4000)
N = int(sys.stdin.readline())
adj_list = [[] for _ in range(N)]
for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  a -= 1
  b -= 1
  adj_list[a].append(b)
  adj_list[b].append(a)

stack = [0]
visit = [False for _ in range(N)]
dist_from_cycle = [-1 for _ in range(N)]

def dfs(cnt):
  cur_node = stack[-1]
  for i in range(len(adj_list[cur_node])):
    nxt = adj_list[cur_node][i]
    if not visit[nxt]:
      visit[nxt] = True
      stack.append(nxt)
      result = dfs(cnt + 1)
      if result: return result
      stack.pop()
    elif nxt != stack[-2]:
      #print(stack)
      return stack[stack.index(nxt):]

visit[0] = True
cycle = dfs(0)
#print(cycle)
for node in cycle:
  dist_from_cycle[node] = 0

def calc_dist_from_cycle(node):
  que = deque()
  visit = [False for _ in range(N)]
  que.append((node, 0))
  visit[node] = True
  while que:
    cur_node, dist = que.popleft()
    if dist_from_cycle[cur_node] == 0:
      return dist
    for i in range(len(adj_list[cur_node])):
      nxt = adj_list[cur_node][i]
      if visit[nxt]:
        continue
      que.append((nxt, dist + 1))
      visit[nxt] = True

for i in range(len(dist_from_cycle)):
  if dist_from_cycle[i] == -1:
    dist_from_cycle[i] = calc_dist_from_cycle(i)
print(*dist_from_cycle)