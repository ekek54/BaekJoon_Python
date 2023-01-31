import sys

N, K = map(int, sys.stdin.readline().split())
hand_sign_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
KH = list(map(int, sys.stdin.readline().split()))
MH = list(map(int, sys.stdin.readline().split()))
for i in range(20):
  KH[i] -= 1
  MH[i] -= 1
JW = []
visit = [False for i in range(N)]
JKM = [JW, KH, MH]
ans = 0


def is_A_win(A, A_idx, B, B_idx):
  if hand_sign_board[JKM[A][A_idx]][JKM[B][B_idx]] == 2:
    return True
  elif hand_sign_board[JKM[A][A_idx]][JKM[B][B_idx]] == 0:
    return False
  else:
    if A > B:
      return True
    else:
      return False


def check():
  # 게임 참여자
  # 0: 지오, 1: 경희, 2: 민호
  JKM_win_list = [0, 0, 0]
  # 지오, 경희, 민호의 다음번에 낼 손모양 배열의 인덱스
  JKM_idx_list = [0, 0, 0]
  A = 0
  B = 1
  while True:
    if is_A_win(A, JKM_idx_list[A], B, JKM_idx_list[B]):
      JKM_idx_list[A] += 1
      JKM_idx_list[B] += 1
      JKM_win_list[A] += 1
      for i in range(3):
        if i != A and i != B:
          B = i
          break
    else:
      JKM_idx_list[A] += 1
      JKM_idx_list[B] += 1
      JKM_win_list[B] += 1
      for i in range(3):
        if i != A and i != B:
          A = i
          break
    if K in JKM_win_list:
      return JKM_win_list.index(K)
    if JKM_idx_list[0] >= N:
      return -1


def dfs(cnt):
  global ans
  if cnt == N:
    if check() == 0:
      ans = 1
    return

  for i in range(N):
    if ans:
      break
    if visit[i]:
      continue
    JW.append(i)
    visit[i] = True
    dfs(cnt + 1)
    JW.pop()
    visit[i] = False


dfs(0)
print(ans)
