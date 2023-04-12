import sys

for _ in range(3):
  N = int(sys.stdin.readline())
  prices = [0]
  cnts = [0]
  value = 0
  for __ in range(N):
    p, cnt = map(int, sys.stdin.readline().split())
    prices.append(p)
    cnts.append(cnt)
    value += (p * cnt)
  if value % 2 == 1:
    print(0)
  else:
    goal = value // 2
    pre = [0 for i in range(goal + 1)]
    cur = [0 for i in range(goal + 1)]
    pre[0] = 1
    done = False
    for i in range(1, len(prices)):
      for j in range(goal + 1):
        for k in range(cnts[i] + 1):
          if j - prices[i] * k >= 0:
            if pre[j - prices[i] * k]:
              cur[j] = 1
              break
          else:
            break
        if cur[goal]:
          done = True
          break
      pre, cur = cur, pre
      if done: break
    #print(pre)
    print(pre[goal] if not pre[goal] else 1)
