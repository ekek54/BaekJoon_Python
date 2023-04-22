import sys

l, w, h = map(int, sys.stdin.readline().split())
v = l * w * h
N = int(sys.stdin.readline())
cubes = []
for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  a = 2 ** a
  cubes.append([a, b])

cubes.sort(key=lambda x: -x[0])


def greedy(l, w, h):
  #print(l, w, h)
  if 0 in (l, w, h):
    return 0

  l, w, h = sorted((l, w, h))
  cur_cube_idx = -1
  for idx, cube in enumerate(cubes):
    cube_len, cube_cnt = cube
    #print(cube_len, cube_cnt)
    if cube_len <= l and cube_cnt > 0:
      cur_cube_idx = idx
      break

  if cur_cube_idx == -1:
    #print('false', l, w, h)
    return -1
  #print(cubes[cur_cube_idx])
  cur_cube_len = cubes[cur_cube_idx][0]
  cur_cube_used = min(h // cur_cube_len, cubes[cur_cube_idx][1])
  cubes[cur_cube_idx][1] -= cur_cube_used
  res = cur_cube_used
  top = greedy(cur_cube_len, cur_cube_len, h - (cur_cube_len * cur_cube_used))
  front = greedy(l - cur_cube_len, cur_cube_len, h)
  right = greedy(cur_cube_len, w - cur_cube_len, h)
  corner = greedy(l - cur_cube_len, w - cur_cube_len, h)
  if -1 in (top, front, right, corner):
    return -1
  res += top + front + right + corner
  #print('res', res)
  return res

answer = greedy(l, w, h)
print(answer)