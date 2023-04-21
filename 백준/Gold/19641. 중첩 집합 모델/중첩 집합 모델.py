import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
adj_list = [[] for _ in range(N)]
answer = [[0, 0] for _ in range(N)]
for _ in range(N):
  arr = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
  src = arr[0]
  childs = arr[1: -1]
  childs.sort()
  for child in childs:
    adj_list[src].append(child)
visit = [False for _ in range(N)]
root = int(sys.stdin.readline()) - 1

cnt = 1
def dfs(node):
  global cnt
  answer[node][0] = cnt
  cnt += 1

  for nxt in adj_list[node]:
    if visit[nxt]: continue
    visit[nxt] = True
    dfs(nxt)

  answer[node][1] = cnt
  cnt += 1

visit[root] = True
dfs(root)
for i in range(N):
  print(i + 1, *answer[i])