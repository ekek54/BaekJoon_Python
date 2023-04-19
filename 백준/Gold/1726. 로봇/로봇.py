import sys
from collections import deque


def conv_to_my_di(input_di):
  if input_di == 1:
    return 0
  if input_di == 2:
    return 2
  if input_di == 3:
    return 1
  if input_di == 4:
    return 3


N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
start_r, start_c, start_di = map(int, sys.stdin.readline().split())
start_r -= 1
start_c -= 1
start_di = conv_to_my_di(start_di)

end_r, end_c, end_di = map(int, sys.stdin.readline().split())
end_r -= 1
end_c -= 1
end_di = conv_to_my_di(end_di)

dist = [[[0 for k in range(4)] for j in range(M)] for i in range(N)]
visit = [[[False for k in range(4)] for j in range(M)] for i in range(N)]
# 우, 하, 좌, 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
que = deque()

def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')

visit[start_r][start_c][start_di] = True
que.append((start_r, start_c, start_di))
while que:
  #pb(visit)
  #pb(dist)
  cur_r, cur_c, cur_di = que.popleft()
  cur_dist = dist[cur_r][cur_c][cur_di]
  if (cur_r, cur_c, cur_di) == (end_r, end_c, end_di):
    print(dist[cur_r][cur_c][cur_di])
    break
  # 우로 방향전환
  if not visit[cur_r][cur_c][(cur_di + 1) % 4]:
    que.append((cur_r, cur_c, (cur_di + 1) % 4))
    dist[cur_r][cur_c][(cur_di + 1) % 4] = cur_dist + 1
    visit[cur_r][cur_c][(cur_di + 1) % 4] = True
  # 좌로 방향전환
  if not visit[cur_r][cur_c][(cur_di - 1) % 4]:
    que.append((cur_r, cur_c, (cur_di - 1) % 4))
    dist[cur_r][cur_c][(cur_di - 1) % 4] = cur_dist + 1
    visit[cur_r][cur_c][(cur_di - 1) % 4] = True
  # k만큼 이동
  for k in range(1, 4):
    nr = cur_r + dr[cur_di] * k
    nc = cur_c + dc[cur_di] * k
    if 0 <= nr < N and 0 <= nc < M:
      if visit[nr][nc][cur_di]: continue
      if board[nr][nc] == 1: break
      visit[nr][nc][cur_di] = True
      dist[nr][nc][cur_di] = cur_dist + 1
      que.append((nr, nc, cur_di))
