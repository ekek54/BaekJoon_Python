import sys
from collections import deque


def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')


# 입력
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
island_map = [[0 for j in range(N)] for i in range(N)]
island_num = 1

# 섬드에 대한 넘버링
island_map = [[0 for j in range(N)] for i in range(N)]
island_num = 1
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
que = deque()

for i in range(N):
  for j in range(N):
    if island_map[i][j] != 0: continue
    if board[i][j] == 1:
      que.append((i, j))
      island_map[i][j] = island_num
      while que:
        cur_r, cur_c = que.popleft()
        for k in range(4):
          nr = cur_r + dr[k]
          nc = cur_c + dc[k]
          if 0 <= nr < N and 0 <= nc < N:
            if island_map[nr][nc] != 0: continue
            if board[nr][nc] == 1:
              island_map[nr][nc] = island_num
              que.append((nr, nc))
      island_num += 1

# 바다에서 bfs로 최단거리 다리 길이 계산
answer = 10000
for i in range(N):
  for j in range(N):
    if board[i][j] == 0:
      visited_island_cnt = 0
      visit = [[False for l in range(N)] for k in range(N)]
      island_dist = [0 for _ in range(island_num)]
      bridge_len = 0
      que.append((i, j, 0))
      while que:
        cur_r, cur_c, dist = que.popleft()
        if island_map[cur_r][cur_c] != 0:
          island = island_map[cur_r][cur_c]
          if island_dist[island - 1] == 0:
            island_dist[island - 1] = dist
            visited_island_cnt += 1
            if visited_island_cnt == 2:
              answer = min(answer, sum(island_dist))
              que.clear()
              break
          else:
            continue
        for k in range(4):
          nr = cur_r + dr[k]
          nc = cur_c + dc[k]
          if 0 <= nr < N and 0 <= nc < N:
            if visit[nr][nc]: continue
            visit[nr][nc] = True
            que.append((nr, nc, dist + 1))
      # print(i, j)
      # print(island_dist)

# pb(island_map)
print(answer - 1)
