import sys

wheel_list = [
  {'state': list(map(int, list(sys.stdin.readline().rstrip('\n')))), 'left': 6, 'right': 2, 'top': 0, 'visit': False}
  for _
  in
  range(4)]
wheel_size = 8
N = int(sys.stdin.readline())
score = 0


# 톱니바퀴 회전
def rotate(wheel_num, clockwise):
  wheel = wheel_list[wheel_num]
  if clockwise == 1:
    wheel['left'] = (wheel['left'] - 1) % wheel_size
    wheel['right'] = (wheel['right'] - 1) % wheel_size
    wheel['top'] = (wheel['top'] - 1) % wheel_size
  else:
    wheel['left'] = (wheel['left'] + 1) % wheel_size
    wheel['right'] = (wheel['right'] + 1) % wheel_size
    wheel['top'] = (wheel['top'] + 1) % wheel_size


def init_visit():
  for i in range(4):
    wheel_list[i]['visit'] = False


# 회전의 전파후 회전
def propagate(wheel_num, clockwise):
  cur_wheel = wheel_list[wheel_num]
  cur_wheel['visit'] = True
  if 1 <= wheel_num:
    left_wheel = wheel_list[wheel_num - 1]
    if not left_wheel['visit']:
      if cur_wheel['state'][cur_wheel['left']] != left_wheel['state'][left_wheel['right']]:
        propagate(wheel_num - 1, clockwise * -1)
  if wheel_num < 3:
    right_wheel = wheel_list[wheel_num + 1]
    if not right_wheel['visit']:
      if cur_wheel['state'][cur_wheel['right']] != right_wheel['state'][right_wheel['left']]:
        propagate(wheel_num + 1, clockwise * -1)
  rotate(wheel_num, clockwise)
  return


def calc_score():
  return sum([wheel_list[i]['state'][wheel_list[i]['top']] * (2 ** i) for i in range(4)])


for i in range(N):
  init_visit()
  wheel_num, clockwise = map(int, sys.stdin.readline().split())  # 바퀴 번호 1 ~ 4, 시계방향 1, 반시계 -1
  wheel_num -= 1  # 0 ~ 3
  propagate(wheel_num, clockwise)

# 점수 계산
for i in range(4):
  top = wheel_list[i]['top']
  if wheel_list[i]['state'][top] == 1:
    score += 2 ** i

print(calc_score())
