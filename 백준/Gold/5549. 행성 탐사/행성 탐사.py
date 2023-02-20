import sys

M, N = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
board = [sys.stdin.readline().rstrip('\n') for _ in range(M)]
jungle_board = [[0 for j in range(N + 1)] for i in range(M + 1)]
ice_board = [[0 for j in range(N + 1)] for i in range(M + 1)]
ocean_board = [[0 for j in range(N + 1)] for i in range(M + 1)]
for i in range(M):
  for j in range(N):
    if board[i][j] == 'J':
      jungle_board[i + 1][j + 1] = 1
    elif board[i][j] == 'I':
      ice_board[i + 1][j + 1] = 1
    if board[i][j] == 'O':
      ocean_board[i + 1][j + 1] = 1

def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')

def convert_to_sumlist(board):
  for i in range(len(board)):
    sum = 0
    for j in range(len(board[0])):
      sum += board[i][j]
      board[i][j] = sum
  for i in range(len(board[0])):
    sum = 0
    for j in range(len(board)):
      sum += board[j][i]
      board[j][i] = sum


def calc_sum(board, a, b, c, d):
  return board[c][d] - board[a - 1][d] - board[c][b - 1] + board[a - 1][b - 1]

#pb(jungle_board)
#pb(ocean_board)
#pb(ice_board)
convert_to_sumlist(jungle_board)
convert_to_sumlist(ocean_board)
convert_to_sumlist(ice_board)
for k in range(K):
  a, b, c, d = map(int, sys.stdin.readline().split())
  print(calc_sum(jungle_board, a, b, c, d), calc_sum(ocean_board, a, b, c, d), calc_sum(ice_board, a, b, c, d))
