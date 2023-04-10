import sys

K, N, F = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N)]
visit = [False for _ in range(N)]

for _ in range(F):
  a, b = map(int, sys.stdin.readline().split())
  a -= 1
  b -= 1
  adj_list[a].append(b)
  adj_list[b].append(a)

friends = []

is_possible = False

for i in range(len(adj_list)):
  adj_list[i].sort()

def dfs(cnt):
  global is_possible
  if cnt == K - 1:
    is_possible = True
    for i in range(len(friends)):
      friends[i] += 1
      print(friends[i])
    return True
  top = friends[-1]
  for nxt in adj_list[top]:
    if visit[nxt]: continue
    if len(adj_list[nxt]) < K - 1: continue
    is_friend_with_nxt = lambda x: x in adj_list[nxt]
    if False in list(map(is_friend_with_nxt, friends)):
      continue
    friends.append(nxt)
    visit[nxt] = True
    if dfs(cnt + 1): return True
    friends.pop()
    visit[nxt] = False
  return False


for i in range(N):
  if len(adj_list[i]) < K - 1:
    visit[i] = True
    continue
  friends.append(i)
  visit[i] = True
  if dfs(0): break
  friends.pop()


if not is_possible:
  print(-1)