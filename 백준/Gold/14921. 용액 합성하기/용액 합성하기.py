import sys
from math import inf

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
l = 0
r = len(A) - 1
result = inf
while l != r:
  cur = A[l] + A[r]
  if abs(result) > abs(cur):
    result = cur
  if A[l] + A[r] > 0:
    r -= 1
  elif A[l] + A[r] < 0:
    l += 1
  else:
    break
print(result)
