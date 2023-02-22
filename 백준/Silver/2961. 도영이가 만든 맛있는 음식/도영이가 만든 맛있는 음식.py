import sys
from math import inf
N = int(sys.stdin.readline())
ingredients = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
stack = []
answer = inf
def calc_taste(ingredients, stack):
  sour = 1
  for i in stack:
    sour *= ingredients[i][0]
  bitter = sum([ingredients[i][1] for i in stack])
  return abs(sour - bitter)

def dfs(cnt):
  global answer
  if stack:
    #print(stack)
    answer = min(answer, calc_taste(ingredients, stack))
  if cnt == N: return

  for i in range(N):
    if stack and stack[-1] >= i: continue
    stack.append(i)
    dfs(cnt + 1)
    stack.pop()

dfs(0)
print(answer)