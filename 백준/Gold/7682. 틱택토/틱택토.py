import sys

state_dict = {}
visit = [False for _ in range(9)]
state = ['.' for _ in range(9)]


def bingo(state):
  cases = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], [(0, 0), (1, 0), (2, 0)],
           [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)], [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
  state_board = [[state[(i * 3) + j] for j in range(3)] for i in range(3)]
  for case in cases:
    is_bingo = True
    cur = state_board[case[0][0]][case[0][1]]
    if cur == '.': continue
    for rc in case:
      r, c = rc
      if cur != state_board[r][c]:
        is_bingo = False
        break
    if is_bingo:
      return True
  return False

def dfs(cnt):
  if cnt == 9:
    state_dict[''.join(state)] = True
    return

  if cnt > 0 and bingo(state):
    state_dict[''.join(state)] = True
    return

  cur = 'X' if cnt % 2 == 0 else 'O'

  for i in range(9):
    if visit[i]:
      continue
    visit[i] = True
    state[i] = cur
    dfs(cnt + 1)
    state[i] = '.'
    visit[i] = False
dfs(0)

while True:
  input_state = sys.stdin.readline().rstrip('\n')
  if input_state == 'end':
    break
  print('valid' if input_state in state_dict else 'invalid')