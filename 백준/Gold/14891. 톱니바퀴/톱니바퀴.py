import sys

wheel_list = [{'state': list(map(int, list(sys.stdin.readline().rstrip('\n')))), 'left': 6, 'right': 2, 'top': 0} for _
              in
              range(4)]
wheel_size = 8
N = int(sys.stdin.readline())
visit = [False for _ in range(4)]
score = 0


# 톱니바퀴 회전
def rotate(wheel_num, clockwise):
  if clockwise == 1:
    wheel_list[wheel_num]['left'] = (wheel_list[wheel_num]['left'] - 1) % wheel_size
    wheel_list[wheel_num]['right'] = (wheel_list[wheel_num]['right'] - 1) % wheel_size
    wheel_list[wheel_num]['top'] = (wheel_list[wheel_num]['top'] - 1) % wheel_size
  else:
    wheel_list[wheel_num]['left'] = (wheel_list[wheel_num]['left'] + 1) % wheel_size
    wheel_list[wheel_num]['right'] = (wheel_list[wheel_num]['right'] + 1) % wheel_size
    wheel_list[wheel_num]['top'] = (wheel_list[wheel_num]['top'] + 1) % wheel_size


# 회전의 전파후 회전
def propagate(wheel_num, clockwise):
  visit[wheel_num] = True
  if 1 <= wheel_num:
    if not visit[wheel_num - 1]:
      if wheel_list[wheel_num]['state'][wheel_list[wheel_num]['left']] != wheel_list[wheel_num - 1]['state'][
        wheel_list[wheel_num - 1]['right']]:
        propagate(wheel_num - 1, clockwise * -1)
  if wheel_num < 3:
    if not visit[wheel_num + 1]:
      if wheel_list[wheel_num]['state'][wheel_list[wheel_num]['right']] != wheel_list[wheel_num + 1]['state'][
        wheel_list[wheel_num + 1]['left']]:
        propagate(wheel_num + 1, clockwise * -1)
  rotate(wheel_num, clockwise)
  return


for i in range(N):
  visit = [False for _ in range(4)]
  wheel_num, clockwise = map(int, sys.stdin.readline().split())  # 바퀴 번호 1 ~ 4, 시계방향 1, 반시계 -1
  wheel_num -= 1  # 0 ~ 3
  propagate(wheel_num, clockwise)

# 점수 계산
for i in range(4):
  top = wheel_list[i]['top']
  if wheel_list[i]['state'][top] == 1:
    score += 2 ** i

print(score)
