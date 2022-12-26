import sys
import copy

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

zero_cnt = 0
cam_spot = []

for i in range(N):
  for j in range(M):
    if board[i][j] == 0:
      zero_cnt += 1
    elif board[i][j] != 6:
      cam_spot.append([i, j])

cam_cnt = len(cam_spot)

di = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
cam_sights_by_type = {1: ['U', 'D', 'L', 'R'],
                      2: ['UD', 'LR'],
                      3: ['UR', 'RD', 'DL', 'LU'],
                      4: ['ULR', 'RDU', 'DLR', 'LUD'],
                      5: ['UDLR']
                      }

board_stack = [[board, zero_cnt]]
candid = []

def dfs(cnt):
  if cnt == cam_cnt:
    last_zero_cnt = board_stack[-1][1]
    candid.append(last_zero_cnt)
    return

  cur_cam_spot = cam_spot[cnt]
  cur_cam_type = board[cur_cam_spot[0]][cur_cam_spot[1]]
  cur_cam_sights = cam_sights_by_type[cur_cam_type]
  board_stack_top = board_stack[-1]
  for cur_cam_sight in cur_cam_sights:
    cur_board = copy.deepcopy(board_stack_top[0])
    cur_zero_cnt = board_stack_top[1]
    for direction in cur_cam_sight:
      r, c = cur_cam_spot
      while 0 <= r < N and 0 <= c < M:
        if cur_board[r][c] == 0:
          cur_board[r][c] = -1
          cur_zero_cnt -= 1
        elif cur_board[r][c] == 6:
          break
        r += di[direction][0]
        c += di[direction][1]
    board_stack.append([cur_board,cur_zero_cnt])
    dfs(cnt+1)
    board_stack.pop()

dfs(0)
print(min(candid))