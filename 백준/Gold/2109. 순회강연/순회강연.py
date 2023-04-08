import sys

n = int(sys.stdin.readline())
if n == 0:
  print(0)
else:
  requests = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
  requests.sort(key= lambda x: (-x[0], -x[1]))
  max_day = max([pd[1] for pd in requests])
  schedule = [0 for _ in range(max_day)]
  for request in requests:
    p, d = request
    d -= 1
    while d >= 0:
      if not schedule[d]:
        schedule[d] = p
        break
      else: d -= 1
  #print(schedule)
  print(sum(schedule))