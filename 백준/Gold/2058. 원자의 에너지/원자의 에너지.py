import sys
import heapq
from math import inf

N, M = map(int, sys.stdin.readline().split())
atoms = [int(sys.stdin.readline()) for _ in range(N)]
atoms.sort()
protons = [int(sys.stdin.readline()) for _ in range(M)]
dp = [[0, 0] for _ in range(N)]
visit = [False for _ in range(N)]


def top_down(n):
  visit[n] = True
  cur_energy = atoms[n]
  childs = []
  for proton in protons:
    if cur_energy - proton in atoms:
      child = atoms.index(cur_energy - proton)
      if not visit[child]:
        childs.append(child)
    if cur_energy + proton in atoms:
      child = atoms.index(cur_energy + proton)
      if not visit[child]:
        childs.append(child)

  if not childs:
    dp[n][0] = 0
    dp[n][1] = cur_energy
    return dp[n]

  dp[n][1] = cur_energy
  for child in childs:
    child_res = top_down(child)
    dp[n][0] += max(child_res)
    dp[n][1] += child_res[0]
  return dp[n]

answer = 0
for i in reversed(range(N)):
  if visit[i]: continue
  answer += max(top_down(i))

print(answer)
#print(dp)