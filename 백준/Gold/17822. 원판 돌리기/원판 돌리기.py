import sys

N, M, T = map(int, sys.stdin.readline().split())
rotate_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cursors = [0 for _ in range(N)]


def rotate(board_idx, d, k):
  if d == 0:
    cursors[board_idx] = (cursors[board_idx] - k) % M
  if d == 1:
    cursors[board_idx] = (cursors[board_idx] + k) % M


def remove_adj_num():
  result = False
  remove_idxs = []
  for i in range(N):
    cur_board = rotate_board[i]
    for j in range(M):
      cur_idx = (cursors[i] + j) % M
      nxt_idx = (cursors[i] + j + 1) % M
      if cur_board[cur_idx] != -1 and cur_board[cur_idx] == cur_board[nxt_idx]:
        result = True
        remove_idxs.append((i, cur_idx))
        remove_idxs.append((i, nxt_idx))
  for i in range(M):
    for j in range(N - 1):
      if rotate_board[j][(cursors[j] + i) % M] != -1 and rotate_board[j][(cursors[j] + i) % M] == rotate_board[j + 1][
        (cursors[j + 1] + i) % M]:
        result = True
        remove_idxs.append((j, (cursors[j] + i) % M))
        remove_idxs.append((j + 1, (cursors[j + 1] + i) % M))
  for remove_idx in remove_idxs:
    r, c = remove_idx
    rotate_board[r][c] = -1
  return result



def sum_board():
  total = 0
  for i in range(N):
    for j in range(M):
      if rotate_board[i][j] != -1:
        total += rotate_board[i][j]
  return total


def cnt_num_in_board():
  cnt = 0
  for i in range(N):
    for j in range(M):
      if rotate_board[i][j] != -1:
        cnt += 1
  return cnt


def flat():
  cnt = cnt_num_in_board()
  if cnt:
    avg = sum_board() / cnt
  else:
    avg = 0
  for i in range(N):
    for j in range(M):
      if rotate_board[i][j] != -1 and rotate_board[i][j] < avg:
        rotate_board[i][j] += 1
      elif rotate_board[i][j] != -1 and rotate_board[i][j] > avg:
        rotate_board[i][j] -= 1


for t in range(T):
  x, d, k = map(int, sys.stdin.readline().split())
  X = x
  while X <= N:
    rotate(X - 1, d, k)
    X += x
  if remove_adj_num():
    continue
  flat()
print(sum_board())
