import sys

N = int(sys.stdin.readline())
S = [sys.stdin.readline().rstrip('\n') for _ in range(N)]
l = 0
r = N - 1
T = ''
while l <= r:
  if l == r:
    T += S[l]
    break

  if S[l] == S[r]:
    idx = 1
    flag = False
    while l + idx <= r - idx:
      if S[l + idx] < S[r - idx]:
        T += S[l]
        l += 1
        flag = True
        break
      elif S[l + idx] > S[r - idx]:
        T += S[r]
        r -= 1
        flag = True
        break
      else:
        idx += 1
    if not flag:
      T += S[l]
      l += 1
  elif S[l] < S[r]:
    T += S[l]
    l += 1
  else:
    T += S[r]
    r -= 1
answer = ''
for i in range(N):
  if i % 80 == 0 and i != 0:
    answer += '\n'
  answer += T[i]
print(answer)