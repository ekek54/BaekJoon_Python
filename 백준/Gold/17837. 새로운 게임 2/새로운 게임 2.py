import sys

N, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
board_piece_state = [[[] for j in range(N)] for i in range(N)]
# [[r, c, di], ...]
# r, c, di 는 1부터
chesspieces = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
turn_cnt = 0
game_over = False

# r, c, di 0부터로 수정
for i in range(len(chesspieces)):
  chesspieces[i][0] -= 1
  chesspieces[i][1] -= 1
  chesspieces[i][2] -= 1
# 체스말들을 저장하는 배열에 체스말 저장
for piece_num, chesspiece in enumerate(chesspieces):
  r, c, di = chesspiece
  board_piece_state[r][c].append(piece_num)


def OOB(r, c):
  return not (0 <= r < N and 0 <= c < N)


# 이동
def move():
  global game_over
  for piece_num, chesspiece in enumerate(chesspieces):
    #print(board_piece_state)
    r, c, di = chesspiece
    h = board_piece_state[r][c].index(piece_num)
    nr = r + dr[di]
    nc = c + dc[di]
    if OOB(nr, nc) or board[nr][nc] == 2:
      # 방향 전환, 다음 칸 수정
      di = di - 1 if di % 2 == 1 else di + 1
      nr = r + dr[di]
      nc = c + dc[di]
      chesspieces[piece_num] = [r, c, di]
    if OOB(nr, nc) or board[nr][nc] == 2:
      continue
    elif board[nr][nc] == 0:
      board_piece_state[r][c], move_pieces = board_piece_state[r][c][:h], board_piece_state[r][c][h:]
      for move_piece_num in move_pieces:
        chesspieces[move_piece_num][0] = nr
        chesspieces[move_piece_num][1] = nc
      board_piece_state[nr][nc] += move_pieces
    elif board[nr][nc] == 1:
      board_piece_state[r][c], move_pieces = board_piece_state[r][c][:h], board_piece_state[r][c][h:]
      for move_piece_num in move_pieces:
        chesspieces[move_piece_num][0] = nr
        chesspieces[move_piece_num][1] = nc
      board_piece_state[nr][nc] += reversed(move_pieces)
    if not OOB(nr, nc) and len(board_piece_state[nr][nc]) >= 4:
      game_over = True

#print(turn_cnt)
while turn_cnt <= 1000 and not game_over:
  turn_cnt += 1
  move()
print(turn_cnt if turn_cnt <= 1000 else -1)
