import sys

N = int(sys.stdin.readline())
len_dict = {chr(i): 1 + (i - 97) for i in range(97, 123)}
len_dict.update({chr(i): 27 + (i - 65) for i in range(65, 91)})
board = [sys.stdin.readline().rstrip() for _ in range(N)]
edge_list = []
total_len = 0
for i in range(N):
  for j in range(N):
    if board[i][j] == '0': continue
    total_len += len_dict[board[i][j]]
    edge = (i, j, len_dict[board[i][j]])
    edge_list.append(edge)

# print(edge_list)
edge_list.sort(key=lambda x: x[2])
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
  if a < b:
    parent[b] = a
  elif a > b:
    parent[a] = b
  else:
    return False
  return True


for edge in edge_list:
  a, b, l = edge
  if a == b: continue
  if union(a, b):
    # print(a, b)
    total_len -= l

for i in range(N):
  find(i)

print(total_len if len(set(parent)) == 1 else -1)
