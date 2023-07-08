import sys
from collections import deque

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
visit = [False for _ in range(n)]
s = int(sys.stdin.readline()) - 1
que = deque()
que.append(s)
answer = 1
visit[s] = True
while que:
    cur = que.popleft()
    nr = cur + A[cur]
    nl = cur - A[cur]

    if 0 <= nr < n and not visit[nr]:
        visit[nr] = True
        answer += 1
        que.append(nr)
    if 0 <= nl < n and not visit[nl]:
        visit[nl] = True
        answer += 1
        que.append(nl)
print(answer)