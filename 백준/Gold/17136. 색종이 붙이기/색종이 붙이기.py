import sys
import copy

paper_counts = [5 for _ in range(5)]
result = 26
board = [list(map(int,sys.stdin.readline().split())) for _ in range(10)]

def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')

# 특정 좌표를 기준으로 n 크기의 색종이를 붙일 수 있는지 확인
def is_insertable(board, rc, n):
  r, c = rc
  if r + n > 10 or c + n > 10:
    return False
  for i in range(r, r + n):
    for j in range(c, c + n):
      if board[i][j] == 0:
        return False
  return True

def attach(board, rc, n):
  r, c = rc
  for i in range(r, r + n):
    for j in range(c, c + n):
      board[i][j] = 0
  return board

def dettach(board, rc, n):
  r, c = rc
  for i in range(r, r + n):
    for j in range(c, c+n):
      board[i][j] = 1
  return board


def find_target_rc(board):
  for i in range(10):
    for j in range(10):
      if board[i][j] == 1:
        target_rc = (i, j)
        return target_rc

def dfs(board, remain_one_block, cnt):
  #pb(board)
  #print(remain_one_block, cnt)
  global result
  if remain_one_block == 0:
    result = min(result, cnt)
    return

  target_rc = find_target_rc(board)
  #print(target_rc)
  for i in range(5):
    if paper_counts[i] == 0: continue
    if is_insertable(board, target_rc, i + 1):
      paper_counts[i] -= 1
      dfs(attach(board, target_rc, i + 1), remain_one_block - (i + 1) ** 2, cnt + 1)
      dettach(board, target_rc, i + 1)
      paper_counts[i] += 1

one_block_cnt = 0
for i in range(10):
  for j in range(10):
    if board[i][j] == 1:
      one_block_cnt += 1

dfs(board, one_block_cnt, 0)
print(result if result < 26 else -1)