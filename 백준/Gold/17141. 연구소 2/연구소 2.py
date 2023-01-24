import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
combination = []
virus_start_rc_candidates = []
wall_rc_list = []
answer = 200
# 바이러스 시작 가능 위치 리스트 생성
for i in range(N):
  for j in range(N):
    if board[i][j] == 2:
      virus_start_rc_candidates.append(tuple([i, j]))
    if board[i][j] == 1:
      wall_rc_list.append(tuple([i, j]))

# 시작 위치 조합 구하기
def dfs(cnt):
  global answer
  if cnt == M:
    res = check(combination)
    if res >= 0:
      answer = min(answer, res)
  for i in range(len(virus_start_rc_candidates)):
    if combination and i <= combination[-1]:
      continue
    combination.append(i)
    dfs(cnt + 1)
    combination.pop()


# bfs로 바이러스 퍼트려서 다 퍼지는데 걸리는 시간 반환
# 다 안퍼지면 False 반환
def bfs(que):
  dist = [[0 for j in range(N)] for i in range(N)]
  visit = [[False for j in range(N)] for i in range(N)]
  # 벽 위치 방문처리
  for wall_rc in wall_rc_list:
    r, c = wall_rc
    visit[r][c] = True
  # 바이러스 시자 위치 방문처리
  for rc in list(que):
    r, c = rc
    visit[r][c] = True
  dr = [1, -1, 0, 0]
  dc = [0, 0, 1, -1]
  max_time = 0
  while que:
    cur_r, cur_c = que.popleft()
    max_time = max(max_time, dist[cur_r][cur_c])
    for i in range(4):
      nr = cur_r + dr[i]
      nc = cur_c + dc[i]
      if 0 <= nr < N and 0 <= nc < N:
        #print(nr, nc)
        if board[nr][nc] != 1 and not visit[nr][nc]:
          dist[nr][nc] = dist[cur_r][cur_c] + 1
          visit[nr][nc] = True
          que.append(tuple([nr, nc]))
  done = True
  for i in range(N):
    if False in visit[i]:
      done = False
  return max_time if done else -1


# 바이러스 시작위치 조합으로 바이러스 퍼트리기(bfs) 수행
def check(combination):
  que = deque()
  for i in range(len(combination)):
    que.append(virus_start_rc_candidates[combination[i]])
  return bfs(que)
dfs(0)
print(-1 if answer == 200 else answer)