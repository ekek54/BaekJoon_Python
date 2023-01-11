import sys
from math import inf
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
op_cnts = list(map(int, sys.stdin.readline().split()))
stack = []
max_ans = -1000000001
min_ans = inf

def add(a, b):
  return a + b


def minus(a, b):
  return a - b


def mul(a, b):
  return a * b


def div(a, b):
  if a < 0:
    return -(-a // b)
  else:
    return a // b


op_funcs = [add, minus, mul, div]

def calc(stack):
  cur = arr[0]
  for i in range(N-1):
    cur_op = stack[i]
    cur = op_funcs[cur_op](cur, arr[i + 1])
  return cur

def dfs(cnt):
  global min_ans
  global max_ans
  if cnt == N - 1:
    res = calc(stack)
    max_ans = max(max_ans, res)
    min_ans = min(min_ans, res)
    return
  for i in range(4):
    if op_cnts[i] == 0:
      continue
    op_cnts[i] -= 1
    stack.append(i)
    dfs(cnt + 1)
    op_cnts[stack.pop()] += 1

dfs(0)
print(max_ans)
print(min_ans)