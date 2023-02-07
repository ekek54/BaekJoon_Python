import sys

result = 0
board = [2 * i for i in range(20)] + [13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 40, 0]
adj_list = {0: [1], 1: [2], 2: [3], 3: [4], 4: [5], 5: [6, 20], 6: [7], 7: [8], 8: [9], 9: [10], 10: [11, 23],
            11: [12], 12: [13], 13: [14], 14: [15], 15: [16, 25], 16: [17], 17: [18], 18: [19], 19: [31], 20: [21],
            21: [22], 22: [28], 23: [24], 24: [28], 25: [26], 26: [27], 27: [28], 28: [29], 29: [30], 30: [31],
            31: [32]}
horses = [0 for _ in range(4)]
dice_list = list(map(int, sys.stdin.readline().split()))
score = 0
#for i, k in enumerate(board):
#  print(i, k)
def dfs(cnt):
  global score, result
  if cnt == 10:
    # 최대값 갱신
    #print(score)
    #print(horses)
    result = max(result, score)
    return

  for i in range(4):
    horse_cur_spot = horses[i]
    horse_nxt_spot = horses[i]
    # 도착지점에 있는 말 가지치기
    if horse_cur_spot == 32:
      continue

    # 댜음 지점 구하기
    for j in range(dice_list[cnt]):
      # 시작지점이 갈림길이면 갈림길로
      if j == 0 and len(adj_list[horse_nxt_spot]) == 2:
        horse_nxt_spot = adj_list[horse_nxt_spot][1]
      else:
        horse_nxt_spot = adj_list[horse_nxt_spot][0]
      # 가다가 도착 지점이면
      if horse_nxt_spot == 32:
        break
    # 다음 지점이 도착 지점이 아니고 다른 말이 있으면 가지치기
    if horse_nxt_spot != 32 and horse_nxt_spot in horses:
      continue

    horses[i] = horse_nxt_spot
    score += board[horse_nxt_spot]
    dfs(cnt + 1)
    horses[i] = horse_cur_spot
    score -= board[horse_nxt_spot]

dfs(0)
print(result)