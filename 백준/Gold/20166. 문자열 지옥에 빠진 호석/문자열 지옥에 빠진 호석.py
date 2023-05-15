import sys
from collections import deque


N, M, K = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(N)]
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
cache = {}

def dfs(rc, cnt, target_str):
    cur_r, cur_c = rc
    if cnt == len(target_str):
        return 1
    result = 0
    for i in range(8):
        nr = (cur_r + dr[i]) % N
        nc = (cur_c + dc[i]) % M
        if board[nr][nc] == target_str[cnt]:
            result += dfs((nr, nc), cnt + 1, target_str)
    return result

def calc_case(target_str):
    start_char = target_str[0]
    result = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == start_char:
                result += dfs((i, j), 1, target_str)
    return result

for _ in range(K):
    target_str = sys.stdin.readline().rstrip()
    if target_str in cache:
        print(cache[target_str])
    else:
        cache[target_str] = calc_case(target_str)
        print(cache[target_str])