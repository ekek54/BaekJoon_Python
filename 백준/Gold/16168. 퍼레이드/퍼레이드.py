import sys

V, E = map(int, sys.stdin.readline().split())
degrees = [0 for _ in range(V)]
parent = [i for i in range(V)]


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


for _ in range(E):
  a, b = map(int, sys.stdin.readline().split())
  a -= 1
  b -= 1
  union(a, b)
  degrees[a] += 1
  degrees[b] += 1
for i in range(V):
  find(i)
if len(set(parent)) > 1:
  print('NO')
else:
  odd_degrees_cnt = list(map(lambda x: x % 2 == 1, degrees)).count(True)
  if odd_degrees_cnt in (0, 2):
    print('YES')
  else:
    print('NO')
