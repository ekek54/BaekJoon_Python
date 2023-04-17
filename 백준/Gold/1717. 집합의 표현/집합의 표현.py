import sys
sys.setrecursionlimit(1000010)

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]
def find(a):
  if a == parent[a]:
    return a
  else:
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
  a = find(a)
  b = find(b)
  if a <= b:
    parent[b] = a
  else:
    parent[a] = b

def in_same_set(a, b):
  a = find(a)
  b = find(b)
  if a == b:
    return True
  else:
    return False

for _ in range(m):
  op, a, b = map(int, sys.stdin.readline().split())
  if op == 1:
    print('YES' if in_same_set(a, b) else 'NO')
  else:
    union(a, b)
