import sys

N = int(sys.stdin.readline())
dp = [[[-1 for k in range(1024)] for j in range(10)] for i in range(N)]


def top_down(i, j, used):
  #print(i,j, used)
  bit = list(bin(used).lstrip('0b').zfill(10))
  #print(bit)
  if i < 0 or j < 0 or 9 < j:
    return 0
  if dp[i][j][used] != -1:
    return dp[i][j][used]
  if bit[j] == '0':
    dp[i][j][used] = 0
    return 0
  if i == 0 and j == 0:
    dp[i][j][used] = 0
    return 0
  if bit.count('1') > i + 1:
    dp[i][j][used] = 0
    return 0

  if i == 0 and bit[j] == '1':
    dp[i][j][used] = 1
    return dp[i][j][used]

  ret = 0
  bit[j] = '0'
  used_xcur = int(''.join(bit), 2)
  ret += top_down(i - 1, j - 1, used)
  ret += top_down(i - 1, j - 1, used_xcur)
  ret += top_down(i - 1, j + 1, used)
  ret += top_down(i - 1, j + 1, used_xcur)
  dp[i][j][used] = ret
  return ret


answer = sum([top_down(N - 1, i, 1023) for i in range(10)])
print(answer % 1000000000)
