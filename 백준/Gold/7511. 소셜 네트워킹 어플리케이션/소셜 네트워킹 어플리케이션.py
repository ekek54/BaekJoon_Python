import sys


def find(a, root_list):
  if root_list[a] == a:
    return a
  else:
    root_list[a] = find(root_list[a], root_list)
    return root_list[a]


def union(a, b, root_list):
  a = find(a, root_list)
  b = find(b, root_list)
  if a < b:
    root_list[b] = a
  else:
    root_list[a] = b


T = int(sys.stdin.readline())
for t in range(T):
  n = int(sys.stdin.readline())
  root_list = [i for i in range(n)]
  k = int(sys.stdin.readline())
  for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
    union(a, b, root_list)
  m = int(sys.stdin.readline())
  print('Scenario', str(t + 1) + ':')
  #print(root_list)
  for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    if find(u, root_list) == find(v, root_list):
      print(1)
    else:
      print(0)
  print("")