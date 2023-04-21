import sys
import math
max_hp_limit = 999999000001 * 123456
N, init_atk = map(int, sys.stdin.readline().split())
rooms = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# print(math.log(max_hp_limit, 2)) = 56
l = 1
r = max_hp_limit

def simul(tmp_max_hp):
  cur_hp = tmp_max_hp
  cur_atk = init_atk
  for room in rooms:
    t, a, h = room
    if t == 1:
      cur_hp -= ((h - 1) // cur_atk) * a
      if cur_hp <= 0:
        return False
    if t == 2:
      cur_atk += a
      cur_hp += h
      cur_hp = min(cur_hp, tmp_max_hp)
  return True

while l <= r:
  mid = (l + r) // 2
  if simul(mid):
    r = mid - 1
  else:
    l = mid + 1

print(l)