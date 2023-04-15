import sys
sys.setrecursionlimit(250000)
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visit = [[False for j in range(N)] for i in range(N)]
dist = [[0 for j in range(N)] for i in range(N)]
stack = []
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def oob(r, c):
  return not (0 <= r < N and 0 <= c < N)


def dfs(cnt):
  cur_r, cur_c = stack[-1]
  if visit[cur_r][cur_c]: return dist[cur_r][cur_c]

  nxts = []
  for i in range(4):
    nr = cur_r + dr[i]
    nc = cur_c + dc[i]
    if oob(nr, nc): continue
    if board[nr][nc] <= board[cur_r][cur_c]: continue
    nxts.append((nr, nc))
  if not nxts:
    return 0

  visit[cur_r][cur_c] = True
  for nxt in nxts:
    nr, nc = nxt
    stack.append((nr, nc))
    dist[cur_r][cur_c] = max(dist[cur_r][cur_c], dfs(cnt + 1))
    stack.pop()
  dist[cur_r][cur_c] += 1
  return dist[cur_r][cur_c]

for i in range(N):
  for j in range(N):
    if visit[i][j]: continue
    stack.append((i, j))
    dfs(0)
    stack.pop()

def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')
print(max(map(max,dist)) + 1)