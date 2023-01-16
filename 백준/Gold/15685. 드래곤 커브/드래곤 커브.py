from sys import stdin
from copy import deepcopy

N = int(stdin.readline())
board = [[0 for j in range(101)] for i in range(101)]


# 1세대 증가
def upgrade(dragon_curve):
  #print(dragon_curve)
  upgrade_cords = []

  end_r, end_c = dragon_curve["end"]
  new_end_r, new_end_c = [end_c, 100 - end_r]
  r_gap = new_end_r - end_r
  c_gap = new_end_c - end_c

  start_r, start_c = dragon_curve["start"]
  next_end = [start_c - r_gap, 100 - start_r - c_gap]

  for cord in dragon_curve["cords"]:
    new_r = cord[1] - r_gap
    new_c = (100 - cord[0]) - c_gap
    if tuple([new_r, new_c]) not in dragon_curve["cords"]:
      #print(cord)
      #print(tuple([new_r, new_c]))
      upgrade_cords.append(tuple([new_r, new_c]))
  dragon_curve["end"] = next_end
  dragon_curve["cords"] += upgrade_cords
  return dragon_curve


def draw_dragon_curve(start_r, start_c, start_d, g):
  dr = [0, -1, 0, 1]
  dc = [1, 0, -1, 0]
  end_r = start_r + dr[start_d]
  end_c = start_c + dc[start_d]
  dragon_curve = {
    "start": [start_r, start_c],
    "end": [end_r, end_c],
    "cords": []
  }
  dragon_curve["cords"].append(tuple([start_r, start_c]))
  dragon_curve["cords"].append(tuple([end_r, end_c]))
  for i in range(g):
    dragon_curve = upgrade(dragon_curve)
  for cord in dragon_curve["cords"]:
    cord_r, cord_c = cord
    board[cord_r][cord_c] = 1


def check(board):
  cnt = 0
  for i in range(100):
    for j in range(100):
      if board[i][j] and board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
        cnt += 1
  return cnt

def pb(board):
  for i in range(len(board)):
    print(board[i])


for i in range(N):
  x, y, d, g = map(int, stdin.readline().split())
  draw_dragon_curve(y, x, d, g)
  #pb(board)
print(check(board))
