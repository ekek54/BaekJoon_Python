import sys
T = int(sys.stdin.readline())

def isprefix(pre, cur):
  len_pre = len(pre)
  if len(pre) > len(cur):
    return False
  return cur[:len_pre] == pre

for t in range(T):
  N = int(sys.stdin.readline())
  numbers = [sys.stdin.readline().rstrip('\n') for _ in range(N)]
  numbers.sort()
  answer = 'YES'
  for i in range(1, N):
    pre_number = numbers[i - 1]
    cur_number = numbers[i]
    if isprefix(pre_number, cur_number):
      answer = 'NO'
      break
  print(answer)
