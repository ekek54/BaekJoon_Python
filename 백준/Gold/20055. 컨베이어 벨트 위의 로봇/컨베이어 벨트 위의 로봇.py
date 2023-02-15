import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
A = deque(list(map(int, sys.stdin.readline().split())))
robots = deque([False for _ in range(N)])
RAISE = 0
LOWER = N - 1
answer = 0


def rotate():
  A.appendleft(A.pop())
  robots.pop()
  robots.appendleft(False)
  if robots[LOWER]:
    robots[LOWER] = False


def robot_move():
  global K
  for i in reversed(range(1, N)):
    if robots[i - 1] and (not robots[i]) and A[i] >= 1:
      robots[i] = True
      robots[i - 1] = False
      A[i] -= 1
      if A[i] == 0:
        K -= 1


def raise_robot():
  global K
  if A[RAISE] != 0:
    robots[RAISE] = True
    A[RAISE] -= 1
    if A[RAISE] == 0:
      K -= 1


while K > 0:
  rotate()
  robot_move()
  raise_robot()
  answer += 1

print(answer)