import sys

N, M = map(int, sys.stdin.readline().split())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
robot_r, robot_c, robot_d = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 0


def within_range(r, c):
  return 0 <= r < N and 0 <= c < M


while True:
  if board[robot_r][robot_c] == 0:
    board[robot_r][robot_c] = -1
    cnt += 1
  no_place_to_clean = True
  for i in range(1, 5):
    nd = (robot_d - i) % 4
    nr = robot_r + dr[nd]
    nc = robot_c + dc[nd]
    if within_range(nr, nc) and board[nr][nc] == 0:
      robot_r = nr
      robot_c = nc
      robot_d = nd
      no_place_to_clean = False
      break
  if no_place_to_clean:
    nr = robot_r - dr[robot_d]
    nc = robot_c - dc[robot_d]
    if within_range(nr, nc) and board[nr][nc] != 1:
      robot_r = nr
      robot_c = nc
    else:
      break
print(cnt)
