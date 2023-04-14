import sys

N, M = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
answer = 0


def oob(r, c):
  return not (0 <= r < N and 0 <= c < M)


def single(rc, size, visit):
  r, c = rc
  nxts = []
  for i in range(4):
    nr = r + size * dr[i]
    nc = c + size * dc[i]
    if oob(nr, nc): continue
    if visit[nr][nc]: continue
    if board[nr][nc] == '.': continue
    nxts.append((nr, nc))
  if len(nxts) == 4:
    for nxt in nxts:
      nr, nc = nxt
      visit[nr][nc] = True
    return True
  else:
    return False


def area(size):
  return 4 * (size - 1) + 1


def double(main_rc, sub_rc):
  visit = [[False for j in range(M)] for i in range(N)]
  main_r, main_c = main_rc
  visit[main_r][main_c] = True
  sub_r, sub_c = sub_rc
  visit[sub_r][sub_c] = True
  main_flag = True
  sub_flag = True
  main_size = 1
  sub_size = 1
  while main_flag or sub_flag:
    if main_flag:
      if single(main_rc, main_size, visit):
        main_size += 1
      else:
        main_flag = False

    if sub_flag:
      if single(sub_rc, sub_size, visit):
        sub_size += 1
      else:
        sub_flag = False
  return area(main_size) * area(sub_size)


for i in range(N * M - 1):
  r1, c1 = i // M, i % M
  rc1 = (r1, c1)
  if board[r1][c1] == '.': continue
  for j in range(i + 1, N * M):
    r2, c2 = j // M, j % M
    rc2 = (r2, c2)
    if board[r2][c2] == '.': continue
    # print(double(rc1, rc2), double(rc2, rc1))
    answer = max(double(rc1, rc2), double(rc2, rc1), answer)

print(answer)
