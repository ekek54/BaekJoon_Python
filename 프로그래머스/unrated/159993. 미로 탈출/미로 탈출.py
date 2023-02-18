from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
    def bfs(src, des):
        que = deque()
        visit = [[False for j in range(M)] for i in range(N)]
        dist = [[0 for j in range(M)] for i in range(N)]
        que.append(src)
        visit[src[0]][src[1]] = True
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        while que:
            cur_r, cur_c = que.popleft()
            if (cur_r, cur_c) == des:
                return dist[cur_r][cur_c]
            for i in range(4):
                nr = cur_r + dr[i]
                nc = cur_c + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    if not visit[nr][nc] and maps[nr][nc] != 'X':
                        visit[nr][nc] = True
                        dist[nr][nc] = dist[cur_r][cur_c] + 1
                        que.append((nr, nc))
        return False
    s_to_l = bfs(start, lever)
    l_to_e = bfs(lever, end)
    if s_to_l and l_to_e:
        return s_to_l + l_to_e
    return -1