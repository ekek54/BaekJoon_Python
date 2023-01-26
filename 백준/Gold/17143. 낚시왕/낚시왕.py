import sys

R, C, M = map(int, sys.stdin.readline().split())
shark_dict = {}

# 상, 하, 우, 좌
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
board = [[0 for j in range(C)] for i in range(R)]

for i in range(M):
  r, c, s, d, z = map(int, sys.stdin.readline().split())
  shark_dict[z] = {"di": d - 1, "speed": s}
  board[r - 1][c - 1] = z

size_sum = 0
for i in range(C):
  # 잡는다!
  #print(board)
  for j in range(R):
    if board[j][i]:
      size_sum += board[j][i]
      #print(size_sum)
      board[j][i] = 0
      break
  # 상어들 가야 할 칸으로 이동
  # 칸에서 제일 큰애만 살아남는다
  tmp_board = [[0 for j in range(C)] for i in range(R)]
  for j in range(R):
    for k in range(C):
      if board[j][k] == 0:
        continue
      shark_size = board[j][k]
      shark = shark_dict[shark_size]
      #print(shark)
      nr = j + dr[shark["di"]] * (shark["speed"] % (2 * (R - 1)))
      nc = k + dc[shark["di"]] * (shark["speed"] % (2 * (C - 1)))
      # 방향 전환
      while not (0 <= nr < R and 0 <= nc < C):
        if nr < 0:
          shark["di"] = 1
          nr = -1 * nr
        if nc < 0:
          shark["di"] = 2
          nc = -1 * nc
        if nr >= R:
          shark["di"] = 0
          nr = R - 1 - (nr - (R - 1))
        if nc >= C:
          shark["di"] = 3
          nc = C - 1 - (nc - (C - 1))
      tmp_board[nr][nc] = max(tmp_board[nr][nc], shark_size)
  board = tmp_board
print(size_sum)
