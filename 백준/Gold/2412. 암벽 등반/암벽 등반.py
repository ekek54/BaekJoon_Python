import sys
from collections import deque

n, T = map(int, sys.stdin.readline().split())
visit = {(0, 0): False}
flag = False
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    visit[(x, y)] = False
    if y == T: flag = True
if not flag: print(-1)
else:
    que = deque()
    visit[(0, 0)] = True
    que.append((0, 0, 0))
    answer = -1
    while que:
        cur_r, cur_c, dist = que.popleft()
        if cur_c == T:
            answer = dist
            break
        for i in range(-2, 3):
            for j in range(-2, 3):
                nr = cur_r + i
                nc = cur_c + j
                if (nr, nc) in visit and not visit[(nr, nc)]:
                    que.append((nr, nc, dist + 1))
                    visit[(nr, nc)] = True
    print(answer)