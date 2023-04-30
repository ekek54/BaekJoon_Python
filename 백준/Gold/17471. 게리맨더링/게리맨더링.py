import sys
from collections import deque
from math import inf


def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')


N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
adj_list = [[] for _ in range(N)]
for i in range(N):
  input_arr = list(map(int, sys.stdin.readline().split()))
  if len(input_arr) >= 1:
    for adj in input_arr[1:]:
      adj -= 1
      adj_list[i].append(adj)

#print(adj_list)
answer = inf
stack = []


def check(arr):
  if len(set(arr)) == 1:
    return -1
  A = sum(P)
  B = 0
  que = deque()
  A_team = set()
  B_team = set()
  for i in range(N):
    if arr[i] == 0:
      A_team.add(i)
    else:
      B_team.add(i)
  que.append(list(A_team)[0])
  chk_A = set()
  visit = [False for _ in range(N)]
  visit[list(A_team)[0]] = True
  while que:
    cur = que.popleft()
    chk_A.add(cur)
    for nxt in adj_list[cur]:
      if visit[nxt]: continue
      if arr[nxt] == 0:
        visit[nxt] = True
        que.append(nxt)
  if chk_A != A_team:
    return -1

  que.append(list(B_team)[0])
  chk_B = set()
  visit = [False for _ in range(N)]
  visit[list(B_team)[0]] = True
  while que:
    cur = que.popleft()
    chk_B.add(cur)
    B += P[cur]
    for nxt in adj_list[cur]:
      if visit[nxt]: continue
      if arr[nxt] == 1:
        visit[nxt] = True
        que.append(nxt)
  if chk_B != B_team:
    return -1
  #print(A, B)
  return abs(A - 2 * B)


def dfs(cnt):
  global answer
  if cnt == N:
    tmp = check(stack)
    if tmp != -1:
      answer = min(answer, tmp)
    return

  for i in range(2):
    stack.append(i)
    dfs(cnt + 1)
    stack.pop()


dfs(0)
print(answer if answer != inf else -1)
