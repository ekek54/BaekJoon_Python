import sys
from math import inf

N, L, R, X = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
answer = 0
stack = []


def is_possible(stack):
  selected = []
  if stack.count(1) < 2:
    return False
  for i in range(len(stack)):
    if stack[i]:
      selected.append(arr[i])
  if max(selected) - min(selected) >= X and L <= sum(selected) <= R: return True
  return False

def dfs(cnt):
  global answer
  if cnt == N:
    if is_possible(stack):
      answer += 1
    return

  for i in range(2):
    stack.append(i)
    dfs(cnt + 1)
    stack.pop()

dfs(0)
print(answer)