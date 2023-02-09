import sys

# 블록 쌓기
# 꽉찬 열 / 행 확인 후 삭제
# 삭제 된 열 / 행 만큼 이동
# 연한 칸(0, 1) 확인
# 연한 칸 차지하는 행 / 열 만큼 쉬프트

blue_board = [[0 for j in range(6)] for i in range(4)]
green_board = [[0 for j in range(6)] for i in range(4)]
score = 0


# 블록 놓기
def insert_block(t, x, y, board):
  flag = False
  if t == 1:
    for i in range(6):
      if board[x][i] == 1:
        flag = True
        break
    if flag:
      board[x][i - 1] = 1
    else:
      board[x][5] = 1
  elif t == 2:
    for i in range(6):
      if board[x][i] == 1:
        flag = True
        break
    if flag:
      board[x][i - 2] = 1
      board[x][i - 1] = 1
    else:
      board[x][4] = 1
      board[x][5] = 1
  elif t == 3:
    for i in range(6):
      if board[x][i] == 1 or board[x + 1][i] == 1:
        flag = True
        break
    if flag:
      board[x][i - 1] = 1
      board[x + 1][i - 1] = 1
    else:
      board[x][5] = 1
      board[x + 1][5] = 1
  return


# 완성된 줄 삭제 후 이동 점수(삭제된 줄 수) 반환
def check_full_line(board):
  new_board = []
  for i in range(6):
    line = [board[j][i] for j in range(4)]
    if 0 in line:
      new_board.append(line)
  score = 6 - len(new_board)
  if score:
    new_board = [[0 for _ in range(4)] for i in range(score)] + new_board
  new_board = [[new_board[j][i] for j in range(6)] for i in range(4)]
  return (new_board, score)


def check_zero_one_line(board):
  cnt = 0
  for i in range(2):
    line = [board[j][i] for j in range(4)]
    if 1 in line:
      cnt += 1

  if cnt:
    for i in range(4):
      board[i] = [0 for _ in range(cnt)] + board[i][:6 - cnt]



def stacking_block(t, x, y, board):
  global score
  insert_block(t, x, y, board)
  # pb(board)
  board, add_score = check_full_line(board)
  score += add_score
  check_zero_one_line(board)
  return board

def cnt_block(board):
  cnt = 0
  for i in range(4):
    for j in range(6):
      if board[i][j] == 1:
        cnt += 1
  return cnt


def pb(board):
  for i in range(len(board)):
    print(board[i])


N = int(sys.stdin.readline())
for i in range(N):
  t, x, y = map(int, sys.stdin.readline().split())
  blue_board = stacking_block(t, x, y, blue_board)
  if t == 1:
    x, y = 3 - y, x
  elif t == 2:
    t = 3
    x, y = 2 - y, x
  elif t == 3:
    t = 2
    x, y = 3 - y, x
  green_board = stacking_block(t, x, y, green_board)
print(score)
print(cnt_block(blue_board) + cnt_block(green_board))
