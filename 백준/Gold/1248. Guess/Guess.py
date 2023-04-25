import sys

N = int(sys.stdin.readline())
board = [['' for j in range(N)] for i in range(N)]
input_str = sys.stdin.readline()
idx = 0
for i in range(N):
  for j in range(i, N):
    board[i][j] = input_str[idx]
    idx += 1
#print(board)
stack = []
def dfs(cnt):
  if cnt == N:
    return True

  for i in range(-10,11):
    valid = True
    for j in range(cnt + 1):
      partial_sum = sum(stack[j: cnt]) + i if cnt > 0 else i
      #print(partial_sum)
      if board[j][cnt] == '-' and partial_sum >= 0:
        valid = False
        break
      elif board[j][cnt] == '+' and partial_sum <= 0:
        valid = False
        break
      elif board[j][cnt] == '0' and partial_sum != 0:
        valid = False
        break
    if not valid: continue
    stack.append(i)
    if dfs(cnt + 1): return True
    stack.pop()

  return False

dfs(0)
print(*stack)