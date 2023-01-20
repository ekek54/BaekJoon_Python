import sys
from collections import deque

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
shark_size = 2
time = 0
shark_coord = [0, 0]
shark_exp = 0

for i in range(N):
  for j in range(N):
    if board[i][j] == 9:
      shark_coord = [i, j]
      board[i][j] = 0


def oob(r, c):
  return not (0 <= r < N and 0 <= c < N)


def bfs(start):
  dr = [-1, 0, 0, 1]
  dc = [0, -1, 1, 0]
  flag = False
  que = deque()
  que.append([start, 0])
  fish_list = []
  visit = [[False for j in range(N)] for i in range(N)]
  visit[start[0]][start[1]] = True
  while que:
    breaker = False
    # print(que)
    cur, dist = que.popleft()
    cur_r, cur_c = cur
    for i in range(4):
      nxt_r = cur_r + dr[i]
      nxt_c = cur_c + dc[i]
      if oob(nxt_r, nxt_c):
        continue
      elif (board[nxt_r][nxt_c] == 0 or board[nxt_r][nxt_c] == shark_size) and not visit[nxt_r][nxt_c]:
        nxt = [nxt_r, nxt_c]
        que.append([nxt, dist + 1])
        visit[nxt_r][nxt_c] = True
      elif 0 < board[nxt_r][nxt_c] < shark_size:
        if not flag:
          flag = dist + 1
        if flag == dist + 1:
          visit[nxt_r][nxt_c] = True
          fish_list.append([nxt_r, nxt_c])
        if flag < dist + 1:
          breaker = True
          break
    if breaker:
      break
  if fish_list:
    fish_list.sort()
    return [fish_list[0], flag]
  return [False, False]


def move_distanc(shark, fish):
  return abs(shark[0] - fish[0]) + abs(shark[1] - fish[1])


while True:
  nxt_fish, dist = bfs(shark_coord)
  if not nxt_fish:
    break
  time += dist
  nxt_fish_r, nxt_fish_c = nxt_fish
  shark_exp += 1
  if shark_exp == shark_size:
    shark_size += 1
    shark_exp = 0
  board[nxt_fish_r][nxt_fish_c] = 0
  shark_coord = nxt_fish
print(time)
