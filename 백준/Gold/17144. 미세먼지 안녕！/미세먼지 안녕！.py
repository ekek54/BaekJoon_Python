import sys

R, C, T = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
breaker = False
for i in range(R):
  for j in range(C):
    if A[i][j] == -1:
      cleaner_top_rc = tuple([i, j])
      cleaner_bot_rc = tuple([i + 1, j])
      breaker = True
      break
  if breaker:
    break

#print(cleaner_bot_rc, cleaner_top_rc)

def spread(A):
  tmp_board = [[0 for j in range(C)] for i in range(R)]
  for i in range(R):
    for j in range(C):
      if A[i][j] and A[i][j] != -1:
        # 확산된 칸 수
        cnt = 0
        # 확산 될 미세먼지 값
        spread_dust = A[i][j] // 5
        for k in range(4):
          nr = i + dr[k]
          nc = j + dc[k]
          if 0 <= nr < R and 0 <= nc < C and A[nr][nc] != -1:
            cnt += 1
            tmp_board[nr][nc] += spread_dust
        A[i][j] -= (spread_dust * cnt)
  for i in range(R):
    for j in range(C):
      A[i][j] += tmp_board[i][j]
  return A


def cleaner_rotate(A, rc, clockwise):
  clock = [2, 0, 3, 1]
  counterclock = [2, 1, 3, 0]
  if clockwise:
    rotate_di = clock
  else:
    rotate_di = counterclock
  di = 0
  cur_r, cur_c = rc
  tmp = 0
  while True:
    nr = cur_r + dr[rotate_di[di]]
    nc = cur_c + dc[rotate_di[di]]
    # 이동
    if 0 <= nr < R and 0 <= nc < C:
      if A[nr][nc] == -1:
        break
      A[nr][nc], tmp = tmp, A[nr][nc]
      cur_r, cur_c = nr, nc
    # 방향전환
    else:
      di += 1
  return A

time = 0
while time < T:
  spread(A)
  cleaner_rotate(A, cleaner_top_rc, False)
  cleaner_rotate(A, cleaner_bot_rc, True)
  time += 1

ans = 0

for i in range(R):
  for j in range(C):
    if A[i][j] != -1:
      ans += A[i][j]
print(ans)
