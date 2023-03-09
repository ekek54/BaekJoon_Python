import sys

def is_not_relation(a, b):
  if len(a) == len(b):
    c = [0 for _ in range(len(a))]
    for i in range(len(a)):
      c[i] = a[i] + b[i]
    if set(c) == set([1]):
      return True
  return False

def is_possible(paper):
  if len(paper) == 1:
    return True
  n = len(paper)
  mid = n // 2
  l_paper = paper[:mid]
  r_paper = paper[mid + 1:]
  if is_not_relation(l_paper, list(reversed(r_paper))) and is_possible(l_paper) and is_possible(r_paper):
    return True
  else: return False


T = int(sys.stdin.readline())
for t in range(T):
  paper = list(map(int, list(sys.stdin.readline().rstrip())))
  print('YES' if is_possible(paper) else 'NO')