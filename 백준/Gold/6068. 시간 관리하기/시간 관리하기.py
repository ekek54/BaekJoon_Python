import sys

N = int(sys.stdin.readline())
works = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
works.sort(key=lambda x: (-x[1], x[0]))
pre_start_time = 1000001
for work in works:
  need, dead = work
  pre_start_time = min(dead, pre_start_time) - need
print(pre_start_time if pre_start_time >= 0 else -1)