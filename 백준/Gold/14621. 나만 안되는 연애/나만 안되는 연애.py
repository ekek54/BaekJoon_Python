import sys

# 사심 경로는 남초대 여초대 를 연결하는 경로만 해당
# 사심 경로만으로 모든 대학간의 이동이 가능해야 한다.
# 사심 경로가 최소 거리가 되도록 해야한다.

# MST 문제
# 남초 - 여초 를 잇는 경로만을 남긴 후
# 남은 경로들로 MST를 구성한다.

# 입력
N, M = map(int, sys.stdin.readline().split())
is_man = lambda x: x == 'M'
is_man_of_univs = list(map(is_man, sys.stdin.readline().split()))
edge_list = []
answer = 0
for _ in range(M):
  u, v, d = map(int, sys.stdin.readline().split())
  u -= 1
  v -= 1
  # 둘 다 남초거나 여초 이면 스킵
  if is_man_of_univs[u] == is_man_of_univs[v]:
    continue
  edge_list.append((u, v, d))

edge_list.sort(key=lambda x: x[2])

# 유니온 파인드
parent = [i for i in range(N)]


def find(a):
  if parent[a] == a:
    return a
  else:
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
  a = find(a)
  b = find(b)
  if a < b:
    parent[b] = a
    return True
  elif a > b:
    parent[a] = b
    return True
  else:
    return False


def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')


for edge in edge_list:
  u, v, d = edge
  if find(u) != find(v):
    union(u, v)
    answer += d
print(answer if len(set(map(find, parent))) == 1 else -1)
