import sys

N, M = map(int, sys.stdin.readline().split())
times = []
for _ in range(N):
  T = int(sys.stdin.readline())
  times.append(T)

r = max(times) * M
l = 0


def is_done_in(T):
  global M
  cnt = 0
  for time in times:
    cnt += T // time
  return cnt >= M


while l <= r:
  mid = (l + r) // 2
  if not is_done_in(mid):
    l = mid + 1
  else:
    r = mid - 1

print(l)