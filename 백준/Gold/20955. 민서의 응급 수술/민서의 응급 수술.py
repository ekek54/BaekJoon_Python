import sys

N, M = map(int, sys.stdin.readline().split())
parent = [i for i in range(N)]
cnt = 0


def find(a):
  if a == parent[a]:
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


for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())
  u -= 1
  v -= 1
  if not union(u, v):
    cnt += 1
tree_set = set()
for i in range(N):
  tree_set.add(find(i))
print(cnt + len(tree_set) - 1)
