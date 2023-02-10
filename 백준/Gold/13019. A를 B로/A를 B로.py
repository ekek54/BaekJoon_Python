import sys
from collections import deque

A = sys.stdin.readline().rstrip('\n')
B = sys.stdin.readline().rstrip('\n')
A = list(reversed(A))
A_dict = {}
B = list(reversed(B))
result = 0
for a in A:
  if a in A_dict:
    A_dict[a] += 1
  else:
    A_dict[a] = 1

for b in B:
  if b in A_dict:
    A_dict[b] -= 1
  else:
    result = -1
for v in A_dict.values():
  if v != 0:
    result = -1

if result == -1:
  print(result)
else:
  idx = 0
  cnt = 0
  for i in range(len(B)):
    flag = False
    for j in range(idx, len(A)):
      if A[j] == B[i]:
        flag = True
        idx = j + 1
        cnt += 1
        break
    if not flag:
      break
  print(len(A) - cnt)
