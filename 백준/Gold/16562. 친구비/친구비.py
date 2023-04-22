import sys


N, M, k = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
parent = [i for i in range(N)]

def find(a):
  if a == parent[a]:
    return a
  else:
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
  a = find(a)
  b = find(b)
  if A[a] < A[b]:
    parent[b] = a
  elif A[a] > A[b]:
    parent[a] = b
  else:
    if a < b:
      parent[b] = a
    else:
      parent[a] = b

for _ in range(M):
  v, w = map(int, sys.stdin.readline().split())
  v -= 1
  w -= 1
  union(v, w)

for i in range(N):
  find(i)

groups = set(parent)
min_price = sum(map(lambda x: A[x], groups))
print(min_price if min_price <= k else 'Oh no')