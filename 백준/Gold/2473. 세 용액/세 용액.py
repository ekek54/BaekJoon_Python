import sys
from math import inf

N = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))
solutions.sort()
answer = []
answer_sum = inf
for i in range(N):
  l = i + 1
  r = N - 1
  while l < r:
    cur_solustions = [solutions[i], solutions[l], solutions[r]]
    cur_sum = sum(cur_solustions)
    if abs(cur_sum) < answer_sum:
      answer = cur_solustions
      answer_sum = abs(cur_sum)
    if cur_sum == 0:
      break
    elif cur_sum < 0:
      l += 1
    else:
      r -= 1
  if answer_sum == 0:
    break

print(*answer)
