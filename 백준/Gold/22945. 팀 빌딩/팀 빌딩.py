import sys

N = int(sys.stdin.readline())
dev_stat = list(map(int, sys.stdin.readline().split()))
l = 0
r = len(dev_stat) - 1
answer = (r - l - 1) * min(dev_stat[l], dev_stat[r])
while l < r:
  if dev_stat[l] <=  dev_stat[r]:
    l += 1
  else:
    r -= 1
  answer = max(answer, (r - l - 1) * min(dev_stat[l], dev_stat[r]))
print(answer)