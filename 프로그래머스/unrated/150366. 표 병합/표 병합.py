def solution(commands):
  N = 50
  value_board = [["" for j in range(N)] for i in range(N)]
  merge_board = [[(i, j) for j in range(N)] for i in range(N)]
  prompt = []

  def pb(board):
    for i in range(len(board)):
      print(board[i])
    print('')

  def find(rc):
    r, c = rc
    if merge_board[r][c] == (r, c):
      return (r, c)
    else:
      merge_board[r][c] = find(merge_board[r][c])
      return merge_board[r][c]

  def update_rc(rc, value):
    root_r, root_c = find(rc)
    value_board[root_r][root_c] = value
    return

  def update_value(a, b):
    for i in range(N):
      for j in range(N):
        root_r, root_c = find((i, j))
        if value_board[root_r][root_c] == a:
          value_board[root_r][root_c] = b

  def merge(rc1, rc2):
    root_r1, root_c1 = find(rc1)
    root_r2, root_c2 = find(rc2)
    if value_board[root_r1][root_c1] == "" and value_board[root_r2][root_c2] != "":
      merge_board[root_r1][root_c1] = (root_r2, root_c2)
    else:
      merge_board[root_r2][root_c2] = (root_r1, root_c1)

  def unmerge(rc):
    target_root = find(rc)
    group_value = value_board[target_root[0]][target_root[1]]
    target_rcs = []
    for i in range(N):
      for j in range(N):
        root = find((i, j))
        if root == target_root:
          target_rcs.append((i, j))
    #print(target_rcs)
    for target_rc in target_rcs:
      target_r, target_c = target_rc
      merge_board[target_r][target_c] = (target_r, target_c)
      if target_rc == rc:
        value_board[target_r][target_c] = group_value
      else:
        value_board[target_r][target_c] = ""

  def print_rc(rc):
    root_r, root_c = find(rc)
    prompt.append(value_board[root_r][root_c] if value_board[root_r][root_c] != '' else "EMPTY")

  for command in commands:
    #print(command)
    command = command.split()
    if command[0] == "UPDATE":
      if len(command) == 4:
        rc = (int(command[1]) - 1, int(command[2]) - 1)
        value = command[3]
        update_rc(rc, value)
      elif len(command) == 3:
        value1 = command[1]
        value2 = command[2]
        update_value(value1, value2)
    elif command[0] == "MERGE":
      rc1 = (int(command[1]) - 1, int(command[2]) - 1)
      rc2 = (int(command[3]) - 1, int(command[4]) - 1)
      merge(rc1, rc2)
    elif command[0] == "UNMERGE":
      rc = (int(command[1]) - 1, int(command[2]) - 1)
      unmerge(rc)
    elif command[0] == "PRINT":
      rc = (int(command[1]) - 1, int(command[2]) - 1)
      print_rc(rc)
    #pb(value_board)
    #pb(merge_board)
  return prompt
