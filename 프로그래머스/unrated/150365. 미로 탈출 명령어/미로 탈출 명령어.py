import sys
sys.setrecursionlimit(3000)
def solution(n, m, x, y, r, c, k):
    x, y, r, c = map(lambda x: x - 1, [x, y, r, c])
    stack = []
    delta = {'d': (1, 0), 'l': (0, -1), 'r': (0, 1),'u': (-1, 0)}
    moves = 'dlru'
    if (k - (abs(r - x) + abs(c - y))) % 2 != 0: return 'impossible'
    def dfs(rc):
        global answer
        if rc == (r, c) and len(stack) == k:
            answer = ''.join(stack)
            return answer
        if len(stack) == k:
            return
        cur_r, cur_c = rc
        for move in moves:
            nr = cur_r + delta[move][0]
            nc = cur_c + delta[move][1]
            if 0 <= nr < n and 0 <= nc < m:
                if abs(r - nr) + abs(c - nc) > k - len(stack): continue
                stack.append(move)
                if dfs((nr, nc)): return answer
                stack.pop()
    answer  = dfs((x, y))
    return answer if answer else "impossible"