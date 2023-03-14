import sys


def split_team(n, cnt):
  if n < 2:
    return 'A'
  l = n // 2
  r = n - l
  if cnt == 0:
    l_team = 'A' * l
    r_team = 'B' * r
    return l_team + r_team
  else:
    return split_team(l, cnt - 1) + split_team(r, cnt - 1)


N = int(sys.stdin.readline())
for i in range(7):
  if 2 ** i < N:
    print(split_team(N, i))
  else:
    print(split_team(N, 0))
