import sys
import copy
from collections import deque

N, M, D = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
stack = []
answer = 0


def simulation(arrow_combination, board):
  enemy_cnt = 0
  kill_cnt = 0
  for i in range(N):
    for j in range(M):
      if board[i][j] == 1:
        enemy_cnt += 1
  tmp_board = copy.deepcopy(board)
  arrow_array = [0 for _ in range(M)]
  for idx in arrow_combination:
    arrow_array[idx] = 2
  tmp_board.append(arrow_array)
  while True:
    # 궁수 공격
    dr = [0, -1, 0]
    dc = [-1, 0, 1]
    killed_enemy = []
    for i in range(M):
      if tmp_board[N][i] == 2:
        que = deque()
        visit = [[False for _ in range(M)] for j in range(N)]
        que.append((N, i, 0))
        while que:
          cur_r, cur_c, cur_dist = que.popleft()
          if tmp_board[cur_r][cur_c] == 1:
            # tmp_board[cur_r][cur_c] = 0
            killed_enemy.append((cur_r, cur_c))
            # kill_cnt += 1
            # enemy_cnt -= 1
            break
          for j in range(3):
            nr = cur_r + dr[j]
            nc = cur_c + dc[j]
            if 0 <= nr < N and 0 <= nc < M and not visit[nr][nc] and cur_dist + 1 <= D:
              que.append((nr, nc, cur_dist + 1))
              visit[nr][nc] = True
    killed_enemy = set(killed_enemy)
    kill_cnt += len(killed_enemy)
    enemy_cnt -= len(killed_enemy)
    for rc in list(killed_enemy):
      r, c = rc
      tmp_board[r][c] = 0
    # 적 전진
    tmp_board.pop()
    enemy_cnt -= tmp_board.pop().count(1)
    tmp_board = [[0 for _ in range(M)]] + tmp_board
    tmp_board.append(arrow_array)
    if enemy_cnt == 0:
      break
  return kill_cnt


def combination(cnt):
  global answer
  if cnt == 3:
    answer = max(simulation(stack, board), answer)
    return

  for i in range(M):
    if stack and stack[-1] >= i:
      continue
    stack.append(i)
    combination(cnt + 1)
    stack.pop()


combination(0)
print(answer)
