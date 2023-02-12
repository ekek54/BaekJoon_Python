from collections import deque
def solution(maps):
    answer = []
    N = len(maps)
    M = len(maps[0])
    maps = [[int(list(maps[i])[j]) if list(maps[i])[j] != 'X' else -1 for j in range(M)] for i in range(N)]
    que = deque()
    visit = [[False for j in range(M)] for i in range(N)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    for i in range(N):
        for j in range(M):
            if visit[i][j]:
                continue
            if maps[i][j] == -1:
                continue
            que.append((i, j))
            day = maps[i][j]
            visit[i][j] = True
            while que:
                cur_r, cur_c = que.popleft()
                for k in range(4):
                    nr = cur_r + dr[k]
                    nc = cur_c + dc[k]
                    if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] != -1 and not visit[nr][nc]:
                        day += maps[nr][nc]
                        que.append((nr, nc))
                        visit[nr][nc] = True
            answer.append(day)        
                
    return sorted(answer) if len(answer) != 0 else [-1]