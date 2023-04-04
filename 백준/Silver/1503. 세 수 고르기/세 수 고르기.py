import sys
from math import inf

N, M = map(int, sys.stdin.readline().split())
S = list(map(int, sys.stdin.readline().split()))
nums = [True for i in range(2001)]
nums[0] = False
for s in S:
  nums[s] = False
answer = inf

for i in range(1, 1999):
  if nums[i] == False:
    continue
  l = i
  r = 2000
  while l <= r:
    if not nums[l]:
      l += 1
      continue
    if not nums[r]:
      r -= 1
      continue
    xyz = i * l * r
    #print(i, l, r)
    #print(xyz)
    if abs(N - xyz) < answer:
      answer = abs(N - xyz)
      #tmp = xyz
    answer = min(abs(N - xyz), answer)
    if xyz < N:
      l += 1
    else:
      r -= 1
  if answer == 0: break

print(answer)
#print(tmp)