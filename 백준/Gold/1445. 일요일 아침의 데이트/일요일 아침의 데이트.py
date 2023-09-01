import sys
import heapq
from math import inf

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
des = tuple()
src = tuple()
for i in range(N):
    for j in range(M):
        if board[i][j] == 'F':
            des = (i, j)
        if board[i][j] == 'S':
            src = (i, j)

pq = []
dist = [[[inf, inf] for j in range(M)] for i in range(N)]
dist[src[0]][src[1]] = [0, 0]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
# (지나온 쓰레기, 쓰레기 옆, 좌표)
heapq.heappush(pq, (0, 0, src))


def oob(r, c):
    return not (0 <= r < N and 0 <= c < M)


def is_better_way(org_way, new_way):
    org_tg, org_ng = org_way
    new_tg, new_ng = new_way
    return new_tg < org_tg or (new_tg == org_tg and new_ng < org_ng)


def is_ng(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if oob(nr, nc): continue
        if board[nr][nc] == 'g': return True
    return False


while pq:
    cur_tg, cur_ng, cur_rc = heapq.heappop(pq)
    cur_r, cur_c = cur_rc
    if dist[cur_r][cur_c][0] < cur_tg or (dist[cur_r][cur_c][0] == cur_tg and dist[cur_r][cur_c][1] < cur_ng):
        continue
    for i in range(4):
        nr = cur_r + dr[i]
        nc = cur_c + dc[i]
        if oob(nr, nc): continue
        nxt_tg = cur_tg
        nxt_ng = cur_ng
        if board[nr][nc] == 'g':
            nxt_tg += 1
        elif board[nr][nc] == '.' and is_ng(nr, nc):
            nxt_ng += 1
        if is_better_way(dist[nr][nc], (nxt_tg, nxt_ng)):
            dist[nr][nc][0] = nxt_tg
            dist[nr][nc][1] = nxt_ng
            heapq.heappush(pq, (nxt_tg, nxt_ng, (nr, nc)))

def pb(board):
    for i in range(len(board)):
        print(board[i])
    print("")

print(*dist[des[0]][des[1]])

# pb(dist)