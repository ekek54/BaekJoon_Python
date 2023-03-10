import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
di = {'D': (1, 0), 'L': (0, -1), 'R': (0, 1), 'U': (-1, 0)}
visit = [[False for j in range(M)] for i in range(N)]
root_map = [[-1 for j in range(M)] for i in range(N)]


def pb(board):
  for i in range(len(board)):
    print(board[i])
  print('')


def rev_di(di):
  if di == 'D': return 'U'
  if di == 'U': return 'D'
  if di == 'L': return 'R'
  if di == 'R': return 'L'

stack = []
cnt = 0
def dfs(rc):
  global cnt
  global stack
  r, c = rc
  nr = r + di[board[r][c]][0]
  nc = c + di[board[r][c]][1]
  if not visit[nr][nc]:
    stack.append((nr, nc))
    visit[nr][nc] = True
    dfs((nr, nc))
  else:
    if root_map[nr][nc] == -1:
      cnt += 1
      for i in range(len(stack)):
        target_r, target_c = stack[i]
        root_map[target_r][target_c] = cnt
    else:
      for i in range(len(stack)):
        target_r, target_c = stack[i]
        root_map[target_r][target_c] = root_map[nr][nc]
    stack = []
  return


for i in range(N):
  for j in range(M):
    #pb(root_map)
    if visit[i][j]:
      continue
    stack.append((i, j))
    dfs((i, j))
print(cnt)
#pb(root_map)