import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
dp = [[0 for j in range(M)] for i in range(N)]
visit = [[False for j in range(M)] for i in range(N)]
dp[0][0] = 1


def top_down(r, c):
  if (r, c) == (0, 0):
    return 1

  if visit[r][c]:
    return dp[r][c]

  for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    if 0 <= nr < N and 0 <= nc < M:
      if board[nr][nc] > board[r][c]:
        dp[r][c] += top_down(nr, nc)
  visit[r][c] = True
  return dp[r][c]


print(top_down(N - 1, M - 1))
