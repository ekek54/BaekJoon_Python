import sys
from math import inf

# 젊은 날이 최대여야하므로 누락된 값은 행복도는 무한 피로도는 0 으로 처리한다.
N = int(sys.stdin.readline())
days = []
for _ in range(N):
  u, v = tuple(map(int, sys.stdin.readline().split()))
  days.append((u, v))

# k까지가 젊은 날이라 할때,
# 1 ~ k 구간의 최소 행복도 > k + 1 ~ N 구간의 최대 행복도
# 1 ~ k 구간의 최대 피로도 < K + 1 ~ N 구간의 최소 피로도

# 1 ~ k 구간의 최소 행복도 배열
min_u_from_start = [0 for _ in range(N)]
min_u = 1000000001
for i in range(N):
  if days[i][0] != 0:
    min_u = min(min_u, days[i][0])
  min_u_from_start[i] = min_u

# k ~ N 구간의 최대 행복도 배열
max_u_to_end = [0 for _ in range(N)]
max_u = -1
for i in reversed(range(N)):
  if days[i][0] != 0:
    max_u = max(max_u, days[i][0])
  max_u_to_end[i] = max_u

# 1 ~ k 구간의 최대 피로도 배열
max_v_from_start = [0 for _ in range(N)]
max_v = -1
for i in range(N):
  if days[i][1] != 0:
    max_v = max(max_v, days[i][1])
  max_v_from_start[i] = max_v

# k ~ N 구간의 최소 피로도 배열
min_v_to_end = [0 for _ in range(N)]
min_v = 1000000001
for i in reversed(range(N)):
  if days[i][1] != 0:
    min_v = min(min_v, days[i][1])
  min_v_to_end[i] = min_v

answer = -1
for i in reversed(range(N - 1)):
  if (min_u_from_start[i] >= max_u_to_end[i + 1] and max_v_from_start[i] <= min_v_to_end[i + 1]):
    answer = max(answer, i)
print(answer + 1 if answer != -1 else answer)
