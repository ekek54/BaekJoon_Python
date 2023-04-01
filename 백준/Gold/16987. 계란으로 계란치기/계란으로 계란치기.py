import sys

N = int(sys.stdin.readline())
eggs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0
broken = 0


def dfs(cnt):
  global answer
  global broken

  answer = max(answer, broken)

  if cnt == N:
    return

  if eggs[cnt][0] <= 0:
    dfs(cnt + 1)
    return

  for i in range(N):
    if i == cnt: continue
    if eggs[i][0] <= 0: continue
    eggs[i][0] -= eggs[cnt][1]
    if eggs[i][0] <= 0:
      broken += 1
    eggs[cnt][0] -= eggs[i][1]
    if eggs[cnt][0] <= 0:
      broken += 1
    dfs(cnt + 1)
    if eggs[i][0] <= 0:
      broken -= 1
    eggs[i][0] += eggs[cnt][1]
    if eggs[cnt][0] <= 0:
      broken -= 1
    eggs[cnt][0] += eggs[i][1]


dfs(0)

print(answer)
