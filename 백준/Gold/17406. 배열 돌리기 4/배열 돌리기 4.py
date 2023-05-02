import sys
import copy

N, M, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
rotates = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]


def rotate(r, c, s, board):
  r -= 1
  c -= 1
  dr = [0, -1, 0, 1]
  dc = [-1, 0, 1, 0]
  ret = copy.deepcopy(board)
  for i in range(1, s + 1):
    cur_r = r + i
    cur_c = c + i
    tmp = ret[cur_r][cur_c]
    for j in range(4):
      for k in range(2 * i):
        cur_r += dr[j]
        cur_c += dc[j]
        ret[cur_r][cur_c], tmp = tmp, ret[cur_r][cur_c]
  return ret


def array_value(board):
  return min(map(sum, board))


def pb(board):
  for i in range(N):
    print(board[i])
  print('')


visit = [False for _ in range(K)]
answer = 5000


def dfs(cnt, board):
  #pb(board)
  global answer
  if cnt == K:
    answer = min(answer, array_value(board))
    return

  for i in range(K):
    if visit[i]: continue
    visit[i] = True
    r, c, s = rotates[i]
    dfs(cnt + 1, rotate(r, c, s, board))
    visit[i] = False


dfs(0, board)
print(answer)
