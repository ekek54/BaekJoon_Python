import sys
from collections import deque

N = int(sys.stdin.readline())
friends_list = [[] for _ in range(N)]
for _ in range(N - 1):
  u, v = map(int, sys.stdin.readline().split())
  u -= 1
  v -= 1
  friends_list[u].append(v)
  friends_list[v].append(u)

dp = [[0, 1] for _ in range(N)]
visit = [False for _ in range(N)]


# dfs로 트리 탐색시 재귀 depth가 깊어 메모리 초과 발생
def dfs(root):
  friends = friends_list[root]
  for friend in friends:
    if visit[friend]: continue
    visit[friend] = True
    dfs(friend)
    dp[root][0] += dp[friend][1]
    dp[root][1] += min(dp[friend])


# 리프노드를 찾고 리프노드들로부터 bfs 수행
root = 0
que = deque()
in_degrees = [len(friends_list[i]) for i in range(N)]
for i in range(N):
  if in_degrees[i] == 1:
    que.append(i)

while que:
  cur_node = que.popleft()
  root = cur_node
  #print(cur_node)
  #print(dp)
  if in_degrees[cur_node] == 0:
    break
  in_degrees[cur_node] -= 1
  friends = friends_list[cur_node]
  for friend in friends:
    if in_degrees[friend] != 0:
      dp[friend][0] += dp[cur_node][1]
      dp[friend][1] += min(dp[cur_node])
      in_degrees[friend] -= 1
      if in_degrees[friend] == 1:
        que.append(friend)

#print(dp)
print(min(dp[root]))
