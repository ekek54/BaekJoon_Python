import sys

T = int(sys.stdin.readline())
for t in range(T):
  N, M, K = map(int, sys.stdin.readline().split())
  money_list = list(map(int, sys.stdin.readline().split()))
  stolen_money = sum(money_list[:M])
  ans = 0
  for i in range(N):
    if stolen_money < K:
      ans += 1
    if N == M :
      break
    stolen_money = stolen_money - money_list[i % N] + money_list[(i + M) % N]
  print(ans)
