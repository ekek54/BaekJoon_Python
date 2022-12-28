import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
stack = [board]
candidate = []
def rotate(r, board):
  if r == 0:
    return board
  elif r == 90:  # 90 시계방향
    return [[board[N - 1 - j][i] for j in range(N)] for i in range(N)]
  elif r == 180:  # 180
    return [[board[N - 1 - i][N - 1 - j] for j in range(N)] for i in range(N)]
  elif r == 270:  # 270
    return [[board[j][N - 1 - i] for j in range(N)] for i in range(N)]

def acc(board):
  tmp_board = []
  for i in range(N):
    stack = []
    for j in range(N):
      if board[i][j] != 0:
        stack.append(board[i][j])
    while 1:
      if (len(stack) == N):
        break
      stack.append(0)
    tmp_board.append(stack)
  return tmp_board
def moveLeft(board):
  if len(board)==1:
    return board
  tmp_board = []
  for i in range(N):
    j = 0
    stack = []
    while j < N - 1:
      if board[i][j] == board[i][j + 1]:
        stack.append(board[i][j] + board[i][j + 1])
        j += 2
        if j == N - 1:
          stack.append(board[i][j])
      else:
        stack.append(board[i][j])
        j += 1
        if j == N - 1:
          stack.append(board[i][N - 1])
    while 1:
      if(len(stack) == N):
        break
      stack.append(0)
    tmp_board.append(stack)
  return tmp_board


def move(board, di):
  if di == 0:  # 상
    return rotate(90, moveLeft(acc(rotate(270, board))))
  elif di == 1:  # 하
    return rotate(270, moveLeft(acc(rotate(90, board))))
  elif di == 2:  # 좌
    return moveLeft(acc(board))
  elif di == 3:  # 우
    return rotate(180, moveLeft(acc(rotate(180, board))))


def dfs(cnt):
  if cnt == 5:
    candidate.append(max(map(max,stack[-1])))
    return

  for i in range(4):
    stack.append(move(stack[-1],i))
    dfs(cnt+1)
    stack.pop()

dfs(0)
print(max(candidate))