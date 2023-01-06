import sys
from collections import deque

di = [(0, -1), (-1, 0), (0, 1), (1, 0)]
snake = deque([[0, 0]])
snake_di = 2
# 0: 빈 공간
# 1: 사과
# 2: 뱀
N = int(sys.stdin.readline())
board = [[0 for j in range(N)] for i in range(N)]

# 사과 마킹
K = int(sys.stdin.readline())
for i in range(K):
  apple_r, apple_c = map(int, sys.stdin.readline().split())
  board[apple_r-1][apple_c-1] = 1

L = int(sys.stdin.readline())
trans_di_infos = [sys.stdin.readline().rstrip('\n').split() for _ in range(L)]


def whitin_range(r, c):
  return 0 <= r < N and 0 <= c < N


def turn_left():
  return (snake_di - 1) % 4


def turn_right():
  return (snake_di + 1) % 4


# 반환 값
# 0: 사과 없음
# 1: 사과 있음
# 2: 게임 오버
def move():
  #print(snake)
  head_r, head_c = snake[-1]
  nr = head_r + di[snake_di][0]
  nc = head_c + di[snake_di][1]

  # 벽 or 뱀이면 게임 오버
  if not whitin_range(nr, nc) or board[nr][nc] == 2:
    return False

  # 빈공간이면 꼬리 이동
  if board[nr][nc] == 0:
    tail_r, tail_c = snake.popleft()
    board[tail_r][tail_c] = 0

  # 머리 이동
  board[nr][nc] = 2
  snake.append([nr, nc])

  return True


def main():
  global snake_di
  time = 0
  for i in range(L):
    trans_at, trans_di = trans_di_infos[i]
    trans_at = int(trans_at)
    while time < trans_at:
      time += 1
      if not move():
        return time


    if trans_di == 'L':
      snake_di = turn_left()
    elif trans_di == 'D':
      snake_di = turn_right()
  while True:
    time += 1
    if not move():
      return time

print(main())