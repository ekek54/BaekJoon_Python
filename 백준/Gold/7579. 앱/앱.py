import sys
from math import inf

N, M = map(int, sys.stdin.readline().split())
memory = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

'''
dp = [[inf for j in range(M + 1)] for i in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
  dp[i][0] = 0
  cur_mem = memory[i - 1]
  cur_cost = cost[i - 1]
  for j in range(M + 1):
    dp[i][j] = min(dp[i - 1][j], dp[i - 1][max(j - cur_mem, 0)] + cur_cost)
print(dp)
'''

'''
메모리 최적화 (84% 터짐)
이차원 배열에서 두개의 일차원 배열 재사용하는 방식으로 수정
prev = [inf for _ in range(M + 1)]
cur = [inf for _ in range(M + 1)]
prev[0] = 0
for i in range(N):
  cur[0] = 0
  cur_mem = memory[i]
  cur_cost = cost[i]
  for j in range(M + 1):
    cur[j] = min(prev[j], prev[max(j - cur_mem, 0)] + cur_cost)
  #print(cur)
  prev, cur = cur, prev

print(prev[M])
'''

# 기존: dp[i][j]: i번 앱까지 사용하여 j 메모리에 필요한 코스트 최소량
# 개선: dp[i][j]를 i번 앱까지 사용하여 j 코스트 이용해 구할 수 있는 메모리 최대량
# 코스트는 최대 10000까지 사용할 수 있음
cost_sum = sum(cost)
dp = [[0 for j in range(cost_sum + 1)] for i in range(N + 1)]
for i in range(1, N + 1):
  cur_mem = memory[i - 1]
  cur_cost = cost[i - 1]
  for j in range(cost_sum + 1):
    if j - cur_cost < 0:
      dp[i][j] = dp[i - 1][j]
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_cost] + cur_mem)
#print(dp)
for i in range(cost_sum + 1):
  if dp[-1][i] >= M:
    print(i)
    break