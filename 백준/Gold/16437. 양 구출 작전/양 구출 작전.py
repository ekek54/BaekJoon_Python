import sys
sys.setrecursionlimit(130000)
N = int(sys.stdin.readline())
islands = [() for _ in range(N)]
adj_list = [[] for _ in range(N)]
islands[0] = ('R', 0)
for i in range(1, N):
  t, a, p = sys.stdin.readline().split()
  a = int(a)
  p = int(p)
  adj_list[p - 1].append(i)
  islands[i] = (t, a)

answer = 0
wolf_cnt = 0
def dfs(island_num):
  global answer
  global wolf_cnt

  #print(answer, wolf_cnt)
  for nxt_island_num in adj_list[island_num]:
    type, amount = islands[nxt_island_num]
    tmp = wolf_cnt
    if type == 'W':
      wolf_cnt += amount
      dfs(nxt_island_num)
      wolf_cnt = min(wolf_cnt, tmp)
    elif type == 'S':
      if wolf_cnt < amount:
        answer += amount - wolf_cnt
        wolf_cnt = 0
      else:
        wolf_cnt -= amount
      dfs(nxt_island_num)
      wolf_cnt = min(wolf_cnt, tmp)
dfs(0)
print(answer)