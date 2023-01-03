import sys

N, M, r, c, k = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
orders = list(map(int, sys.stdin.readline().split()))
dice_num = [0 for _ in range(6)]
dice_state = {
  'up': 1,
  'right': 3,
  'front': 5
}

di_dict = {
  1: [0, 1],
  2: [0, -1],
  3: [-1, 0],
  4: [1, 0]
}


def roll(di):
  if di == 1:
    tmp = dice_state['up']
    dice_state['up'] = 7 - dice_state['right']
    dice_state['right'] = tmp
  elif di == 2:
    tmp = dice_state['up']
    dice_state['up'] = dice_state['right']
    dice_state['right'] = 7 - tmp
  elif di == 3:
    tmp = dice_state['up']
    dice_state['up'] = dice_state['front']
    dice_state['front'] = 7 - tmp
  elif di == 4:
    tmp = dice_state['up']
    dice_state['up'] = 7 - dice_state['front']
    dice_state['front'] = tmp


for order in orders:
  nr = r + di_dict[order][0]
  nc = c + di_dict[order][1]
  if 0 <= nr < N and 0 <= nc < M:
    r = nr
    c = nc
    roll(order)
    if board[r][c] == 0:
      board[r][c] = dice_num[7 - dice_state['up'] - 1]
    else:
      dice_num[7 - dice_state['up'] - 1] = board[r][c]
      board[r][c] = 0
    #print(dice_num)
    print(dice_num[dice_state['up']-1])
