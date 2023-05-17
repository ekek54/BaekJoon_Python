import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
visit = {}
is_small = {}
for _ in range(M):
    is_small[int(sys.stdin.readline()) - 1] = True
if 1 in is_small: print(-1)
else:
    answer = -1
    que = deque()
    visit[(1, 1)] = 1
    que.append((1, 1))
    while que:
        cur, speed = que.popleft()
        dist = visit[(cur, speed)]
        if cur == N - 1:
            answer = dist
            break
        for i in range(-1, 2):
            nxt_speed = speed + i
            nxt = cur + nxt_speed
            if nxt >= N: continue
            if nxt in is_small: continue
            if (nxt, nxt_speed) in visit: continue
            visit[(nxt, nxt_speed)] = dist + 1
            que.append((nxt, nxt_speed))
    print(answer)