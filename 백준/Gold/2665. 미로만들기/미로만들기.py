import sys
from math import inf
import heapq

def pb(board):
    for i in range(len(board)):
        print(board[i])
    print('')

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N = int(sys.stdin.readline())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
dist = [[inf for j in range(N)] for i in range(N)]
pq = []
dist[0][0] = 0
heapq.heappush(pq, (0, 0, 0))
while pq:
    cur_dist, cur_r, cur_c = heapq.heappop(pq)
    if cur_dist > dist[cur_r][cur_c]:
        continue

    for i in range(4):
        nr = cur_r + dr[i]
        nc = cur_c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] == 0:
                ndist = cur_dist + 1
            else:
                ndist = cur_dist
            if dist[nr][nc] > ndist:
                dist[nr][nc] = ndist
                heapq.heappush(pq, (ndist, nr, nc))

print(dist[N - 1][N - 1])