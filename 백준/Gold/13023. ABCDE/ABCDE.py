import sys

N, M = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N)]
for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  adj_list[a].append(b)
  adj_list[b].append(a)

visit = [False for _ in range(N)]
stack = []
answer = 0

def dfs(cnt):
  if cnt == 4:
    return True

  for adj in adj_list[stack[-1]]:
    if visit[adj]:
      continue
    visit[adj] = True
    stack.append(adj)
    if dfs(cnt + 1): return True
    stack.pop()
    visit[adj] = False

  return False

for i in range(N):
  stack.append(i)
  visit[i] = True
  if dfs(0):
    answer = 1
    break
  stack.pop()
  visit[i] = False

print(answer)