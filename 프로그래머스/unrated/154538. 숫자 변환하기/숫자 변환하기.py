from collections import deque
def solution(x, y, n):
    que = deque()
    que.append((x, 0))
    visit = [False for _ in range(1000001)]
    while que:
        cur, cnt = que.popleft()
        if cur == y: return cnt
        nxts = [cur + n, cur * 2, cur * 3]
        for nxt in nxts:
            if nxt > y: continue
            if visit[nxt]: continue
            visit[nxt] = True
            que.append((nxt, cnt + 1))
    return -1