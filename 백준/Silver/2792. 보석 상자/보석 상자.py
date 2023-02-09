import sys
from math import inf

N, M = map(int, sys.stdin.readline().split())
gems = [int(sys.stdin.readline()) for _ in range(M)]

def div(K):
  result = 0
  for gem in gems:
    result += (gem // K)
    if gem % K != 0:
      result += 1
  return result


l = 1
r = 1000000000
while l <= r:
  mid = (l + r) // 2
  if N < div(mid):
    l = mid + 1
  else:
    r = mid - 1

print(l)
