import sys
import heapq
from math import inf

N = int(sys.stdin.readline())
add = lambda x: x[0] + x[1]
minus = lambda x: x[0] - x[1]
mul = lambda x: x[0] * x[1]
board = [list(sys.stdin.readline().split()) for _ in range(N)]
dr = [1, 0]
dc = [0, 1]
pq = []
op_dict = {'+': add, '-': minus, '*': mul}
answer = []

# 최대값 구하기
dist = [[-inf for j in range(N)] for i in range(N)]
dist[0][0] = int(board[0][0])
pq.append((-dist[0][0], 0, 0))
while pq:
  cur_dist, cur_r, cur_c = heapq.heappop(pq)
  cur_dist = -cur_dist
  if cur_dist < dist[cur_r][cur_c]: continue
  for i in range(2):
    nr = cur_r + dr[i]
    nc = cur_c + dc[i]
    if 0 <= nr < N and 0 <= nc < N:
      if board[nr][nc].isdigit():
        nxt_dist = op_dict[board[cur_r][cur_c]]((cur_dist, int(board[nr][nc])))
      else:
        nxt_dist = cur_dist
      if dist[nr][nc] < nxt_dist:
        dist[nr][nc] = nxt_dist
        heapq.heappush(pq, (-nxt_dist, nr, nc))
answer.append(dist[N - 1][N - 1])

# 최소값 구하기
min_dist = [[inf for j in range(N)] for i in range(N)]
min_dist[0][0] = int(board[0][0])
pq.append((min_dist[0][0], 0, 0))
while pq:
  cur_dist, cur_r, cur_c = heapq.heappop(pq)
  if cur_dist > min_dist[cur_r][cur_c]: continue
  for i in range(2):
    nr = cur_r + dr[i]
    nc = cur_c + dc[i]
    if 0 <= nr < N and 0 <= nc < N:
      if board[nr][nc].isdigit():
        nxt_dist = op_dict[board[cur_r][cur_c]]((cur_dist, int(board[nr][nc])))
      else:
        nxt_dist = cur_dist
      if min_dist[nr][nc] > nxt_dist:
        min_dist[nr][nc] = nxt_dist
        heapq.heappush(pq, (nxt_dist, nr, nc))
answer.append(min_dist[N - 1][N - 1])

def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')

#pb(dist)
#pb(min_dist)
print(*answer)
